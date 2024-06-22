# ViCodePy - A video coder for psychological experiments
#
# Copyright (C) 2024 Esteban Milleret
# Copyright (C) 2024 Rafael Laboissière
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program. If not, see <https://www.gnu.org/licenses/>.

import colour
from abc import abstractmethod
from enum import IntEnum

from PySide6.QtCore import (
    Qt,
    QRectF,
    QLine,
    QPointF,
    QSizeF,
    Signal,
)
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPolygonF,
    QPen,
    QFontMetrics,
)
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QDialog,
    QLineEdit,
    QColorDialog,
    QComboBox,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsRectItem,
    QGraphicsItem,
    QMenu,
    QMessageBox,
    QScrollBar,
)

from .dialog import TimelineLineDialog
from .ticklocator import TickLocator
from .utils import (
    milliseconds_to_seconds,
    seconds_to_milliseconds,
)


class ZoomableGraphicsView(QGraphicsView):
    MARGIN_BOTTOM = 15.0

    def __init__(self, scene: QGraphicsScene, parent=None):
        super().__init__(scene, parent)
        self.zoomFactor = 1.0
        self.zoomStep = 1.2
        self.zoomShift = None
        self.minimum_zoomFactor = 1.0

        vertical_scrollbar = QScrollBar(Qt.Orientation.Vertical, self)
        vertical_scrollbar.valueChanged.connect(
            self.on_vertical_scroll_value_changed
        )
        self.setVerticalScrollBar(vertical_scrollbar)

    def wheelEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if not self.parent().player.media:
                return
            mouse_pos = self.mapToScene(event.position().toPoint()).x()
            if event.angleDelta().y() > 0:
                self.zoomShift = mouse_pos * (1 - self.zoomStep)
                self.zoom_in()
            else:
                self.zoomShift = mouse_pos * (1 - 1 / self.zoomStep)
                self.zoom_out()
            self.zoomShift = None
        else:
            super().wheelEvent(event)

    def on_vertical_scroll_value_changed(self, value):
        if self.parent().timelineScale:
            self.parent().timelineScale.setPos(0, value)

    def zoom_in(self):
        self.zoomFactor *= self.zoomStep
        self.update_scale()

    def zoom_out(self):
        if self.zoomFactor / self.zoomStep >= self.minimum_zoomFactor:
            self.zoomFactor /= self.zoomStep
            self.update_scale()

    def update_scale(self):
        # Update the size of the scene with zoomFactor
        self.scene().setSceneRect(
            0,
            0,
            self.width() * self.zoomFactor,
            self.scene().height(),
        )

        if self.zoomShift:
            previousAnchor = self.transformationAnchor()
            self.setTransformationAnchor(QGraphicsView.NoAnchor)
            self.translate(self.zoomShift, 0)
            self.setTransformationAnchor(previousAnchor)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        # Get the position click from the scene
        map = self.mapToScene(self.scene().sceneRect().toRect())
        x = map.boundingRect().x()

        # Calculate the time of the position click
        time = int(
            (x + event.scenePosition().x())
            * self.parent().duration
            / self.scene().width()
        )

        # During the creation of a new annotation
        if self.parent().currentAnnotation:
            time = self.parent().currentAnnotation.get_time_from_bounding_box(
                time
            )

        # Set time to the video player
        self.parent().player.set_position(time)


class TimeLineWidget(QWidget):
    CSV_HEADERS = ["begin", "end", "duration", "label", "timeline"]
    valueChanged = Signal(int)
    durationChanged = Signal(int)

    def __init__(self, player=None):
        """Initializes the timeline widget"""
        super().__init__(player)
        self._duration = 0
        self._value = 0

        self.selected_timelineLine = None
        self.currentAnnotation: Annotation = None
        self.player = player
        self.scene = QGraphicsScene()
        self.scene.sceneRectChanged.connect(self.on_scene_changed)
        self.scene.selectionChanged.connect(self.on_selection_changed)
        self.timeline_lines: list[TimelineLine] = []
        self.view = ZoomableGraphicsView(self.scene, self)
        self.indicator = None
        self.timelineScale = None

        self.view.setViewportUpdateMode(
            QGraphicsView.ViewportUpdateMode.FullViewportUpdate
        )
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setFrameShape(QGraphicsView.Shape.NoFrame)
        self.view.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.setMouseTracking(True)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

        self.valueChanged.connect(self.on_value_changed)
        self.durationChanged.connect(self.on_duration_changed)

    def on_scene_changed(self, rect):
        # Update annotations
        for timeline_line in self.timeline_lines:
            timeline_line.update_rect_width(rect.width())
            for annotation in timeline_line.annotations:
                annotation.update_rect()

        if self.currentAnnotation:
            self.currentAnnotation.update_rect()

        # Update timelineScale display
        if self.timelineScale:
            # Update indicator
            if self.duration:
                self.timelineScale.indicator.setX(
                    self.value * rect.width() / self.duration
                )
            self.timelineScale.update()

    def on_selection_changed(self):
        if len(self.scene.selectedItems()) == 1 and isinstance(
            self.scene.selectedItems()[0], TimelineLine
        ):
            self.selected_timelineLine = self.scene.selectedItems()[0]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value != self._value:
            self._value = value
            self.valueChanged.emit(value)

    def on_value_changed(self, new_value):
        # First, update the current annotation, if it exists. If the cursor
        # value goes beyond the allowed bounds, bring it back and do not update
        # the other widgets.
        if self.currentAnnotation:
            if (
                self.currentAnnotation.lower_bound
                and new_value < self.currentAnnotation.lower_bound
            ):
                new_value = self.currentAnnotation.lower_bound
            elif (
                self.currentAnnotation.upper_bound
                and new_value > self.currentAnnotation.upper_bound
            ):
                new_value = self.currentAnnotation.upper_bound
                if (
                    self.player.mediaplayer.playbackState()
                    == QMediaPlayer.PlaybackState.PlayingState
                ):
                    self.player.mediaplayer.pause()
            self.currentAnnotation.update_end_time(new_value)

        # Update indicator position
        if self.timelineScale and self.timelineScale.indicator:
            self.timelineScale.indicator.setX(
                new_value * self.scene.width() / self.duration
            )

        if isinstance(self.scene.focusItem(), AnnotationHandle):
            annotation_handle: AnnotationHandle = self.scene.focusItem()
            annotation_handle.change_time(new_value)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration != self._duration:
            self._duration = duration
            self.durationChanged.emit(duration)

    def on_duration_changed(self, new_duration):
        # Update timeline Scale
        self.timelineScale = TimelineScale(self)
        self.update()

    def load_common(self):
        # Recreate timeline
        self.timelineScale = TimelineScale(self)

    def clear(self):
        # Clear timelineScene
        self.scene.clear()
        self.timeline_lines = []

    def handle_annotation(self):
        """Handles the annotation"""
        if not self.selected_timelineLine:
            QMessageBox.warning(self, "Warning", "No timeline selected")
            return
        else:
            if self.currentAnnotation is None:
                can_be_initiate, lower_bound, upper_bound = (
                    Annotation.annotationDrawCanBeInitiate(
                        self.selected_timelineLine.annotations, self.value
                    )
                )
                if can_be_initiate:
                    self.currentAnnotation = Annotation(
                        self,
                        self.selected_timelineLine,
                        lower_bound,
                        upper_bound,
                    )
            else:
                # End the current annotation
                agd = AnnotationGroupDialog(
                    self.currentAnnotation.timeline_line
                )
                agd.exec()

                if agd.result() == AnnotationDialogCode.Accepted:
                    if agd.state == "create":
                        # When creating a new group, create the group and add the
                        # current annotation to it
                        group = AnnotationGroup(
                            len(self.currentAnnotation.timeline_line.groups)
                            + 1,
                            agd.group_name_text.text(),
                            agd.color,
                            self,
                        )
                        group.add_annotation(self.currentAnnotation)
                        self.currentAnnotation.timeline_line.add_group(group)
                    else:
                        # Otherwise, we are selecting an existing group, and will
                        # retrieve the group and add the annotation to it
                        group = agd.combo_box.currentData()
                        group.add_annotation(self.currentAnnotation)
                    self.currentAnnotation.ends_creation()
                    self.currentAnnotation = None
                    self.player.add_annotation_action.setText(
                        "Start annotation"
                    )
                elif agd.result() == AnnotationDialogCode.Aborted:
                    self.currentAnnotation.remove()
                    self.currentAnnotation = None
                    self.player.add_annotation_action.setText(
                        "Start annotation"
                    )
                self.update()

    def handle_timeline_line(self):
        dialog = TimelineLineDialog(self)
        dialog.exec()
        if dialog.result() == AnnotationDialogCode.Accepted:
            self.add_timeline_line(TimelineLine(dialog.get_text(), self))

    def resizeEvent(self, a0):
        if self.timelineScale:
            self.view.update_scale()
        else:
            self.scene.setSceneRect(
                0,
                0,
                self.view.width(),
                TimelineScale.FIXED_HEIGHT + TimelineLine.FIXED_HEIGHT,
            )

        self.update()

    def keyPressEvent(self, event):
        # if key pressed is escape key
        if event.key() == Qt.Key.Key_Escape:
            # Delete annotation
            if self.currentAnnotation is not None:
                confirm_box = AnnotationConfirmMessageBox(self)
                if (
                    confirm_box.result()
                    == AnnotationConfirmMessageBox.DialogCode.Accepted
                ):
                    self.currentAnnotation.remove()
                    self.currentAnnotation = None
                    self.update()

    def add_timeline_line(self, line):
        self.timeline_lines.append(line)
        line.addToScene()

        # Calculate the new height of the scene
        new_height = (
            TimelineScale.FIXED_HEIGHT
            + len(self.timeline_lines) * TimelineLine.FIXED_HEIGHT
            + ZoomableGraphicsView.MARGIN_BOTTOM
        )
        scene_rect = self.scene.sceneRect()
        scene_rect.setHeight(new_height)
        self.scene.setSceneRect(scene_rect)

        # Set maximum height of the widget
        self.setMaximumHeight(int(new_height))


class TimelineLine(QGraphicsRectItem):
    FIXED_HEIGHT: float = 60.0

    def __init__(self, name: str, timeline_widget: TimeLineWidget = None):
        super().__init__()
        self.name = name
        self.timelineWidget = timeline_widget
        self.annotations: list[Annotation] = []
        self.groups: list[AnnotationGroup] = []
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setAcceptHoverEvents(True)
        self.textItem = TimelineLineLabel(self.name, self)

    def addToScene(self):
        """Add the timeline to the scene"""
        # Set Y of the timeline based on the timescale height and the timeline
        # lines heights present on the scene
        self.setPos(
            0,
            self.timelineWidget.timelineScale.rect().height()
            + (len(self.timelineWidget.timeline_lines) - 1) * self.FIXED_HEIGHT,
        )

        # Set the right rect based on the scene width and the height constant
        self.setRect(
            0,
            0,
            self.timelineWidget.scene.width(),
            self.FIXED_HEIGHT,
        )

        # Add line to the scene
        self.timelineWidget.scene.addItem(self)

    def add_group(self, group):
        """Add a group to the timeline line"""
        self.groups.append(group)
        self.groups.sort(key=lambda x: x.name)

    def remove_group(self, group):
        """Remove a group from the timeline line"""
        self.groups.remove(group)

    def add_annotation(self, annotation):
        """Add an annotation to the timeline line"""
        self.annotations.append(annotation)
        self.annotations.sort(key=lambda x: x.startTime)

    def remove_annotation(self, annotation):
        """Remove an annotation to the timeline line"""
        self.annotations.remove(annotation)

    def update_rect_width(self, new_width: float):
        """Update the width of the timeline line"""
        rect = self.rect()
        rect.setWidth(new_width)
        rect_label = self.textItem.rect()
        rect_label.setWidth(new_width)
        self.textItem.setRect(rect_label)
        self.setRect(rect)


class TimelineLineLabel(QGraphicsRectItem):
    FIXED_HEIGHT = 20

    def __init__(self, text: str, parent: TimelineLine = None):
        super().__init__(parent)
        self.text = text
        rect = self.parentItem().rect()
        rect.setHeight(self.FIXED_HEIGHT)
        self.setRect(rect)

    def paint(self, painter, option, widget=...):
        # Draw the rectangle
        self._draw_rect(painter)

        # Draw the text
        self._draw_text(painter)

    def _draw_rect(self, painter):
        """Draw the timeline line label rectangle"""
        # Set Pen and Brush for rectangle
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.gray)
        painter.drawRect(self.rect())

    def _draw_text(self, painter):
        """Draw the timeline line label text"""
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)

        font = painter.font()
        fm = QFontMetrics(font)
        # Calculate the height of the text
        font_height = painter.fontMetrics().height()

        text_width = fm.boundingRect(self.text).width()
        # Get timeline polygon based on the viewport
        timline_line_in_viewport_pos = (
            self.parentItem().timelineWidget.view.mapToScene(
                self.rect().toRect()
            )
        )
        bounding_rect = timline_line_in_viewport_pos.boundingRect()

        # Get the viewport rect
        viewport_rect = self.parentItem().timelineWidget.view.viewport().rect()

        # Calcul the x position for the text
        x_alignCenter = bounding_rect.x() + viewport_rect.width() / 2

        text_position = QPointF(x_alignCenter - text_width / 2, font_height)

        painter.drawText(text_position, self.text)


class Indicator(QGraphicsItem):
    def __init__(self, parent):
        super().__init__(parent)
        if parent.timelineWidget:
            self.timelineWidget: TimeLineWidget = parent.timelineWidget
        self.pressed = False
        self.y = 15
        self.height = 10
        self.poly: QPolygonF = QPolygonF(
            [
                QPointF(-10, self.y),
                QPointF(10, self.y),
                QPointF(0, self.y + self.height),
            ]
        )
        self.line: QLine = QLine(0, self.y, 2, 10000)

        self.setAcceptHoverEvents(True)
        self.setAcceptDrops(True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setZValue(101)

    def paint(self, painter, option, widget=...):
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawLine(self.line)
        painter.drawPolygon(self.poly)

    def calculate_size(self):
        min_x: float = self.poly[0].x()
        max_x: float = self.poly[0].x()

        for i, point in enumerate(self.poly):
            if point.x() < min_x:
                min_x = point.x()
            if point.x() > max_x:
                max_x = point.x()

        return QSizeF(max_x - min_x, self.height)

    def boundingRect(self):
        size: QSizeF = self.calculate_size()
        return QRectF(-10, self.y, size.width(), size.height())

    def focusInEvent(self, event):
        self.pressed = True
        super().focusInEvent(event)
        self.update()

    def focusOutEvent(self, event):
        self.pressed = False
        super().focusOutEvent(event)
        self.update()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        pos: QPointF = event.scenePos()
        if self.pressed:
            time = int(
                pos.x()
                * self.timelineWidget.duration
                / self.parentItem().rect().width()
            )

            # During creation of a new annotation
            if self.timelineWidget and self.timelineWidget.currentAnnotation:
                annotation = self.timelineWidget.currentAnnotation
                if time != annotation.get_time_from_bounding_box(time):
                    # Stop player at the lower or upper bound when they
                    # are passed over
                    self.setPos(self.x(), 0)
                    return

            self.timelineWidget.player.set_position(time)

            if pos.x() < 0:
                self.setPos(0, 0)
            elif pos.x() > self.parentItem().rect().width():
                self.setPos(self.parentItem().rect().width(), 0)
            else:
                self.setPos(pos.x(), 0)

        self.update()


class TimelineScale(QGraphicsRectItem):

    FIXED_HEIGHT: float = 25.0

    def __init__(self, timeline_widget: TimeLineWidget):
        super().__init__()
        self.timelineWidget = timeline_widget
        self.timelineWidget.scene.addItem(self)
        self.indicator = Indicator(self)
        self.setRect(
            QRectF(0, 0, self.timelineWidget.scene.width(), self.FIXED_HEIGHT)
        )

    def paint(self, painter, option, widget=...):
        self._draw_rect(painter)

        if self.timelineWidget.duration != 0:
            self._draw_scale(painter)

    def _draw_rect(self, painter):
        """Draw the background rectangle of the timeline scale"""
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.lightGray)
        self.setRect(
            QRectF(0, 0, self.timelineWidget.scene.width(), self.FIXED_HEIGHT)
        )
        painter.drawRect(self.rect())

    def _draw_scale(self, painter):
        tl = TickLocator()
        min_gap = 0.05
        dur = self.timelineWidget.duration
        wid = self.timelineWidget.scene.width()
        font = painter.font()
        fm = QFontMetrics(font)
        loc = tl.find_locations(
            0, milliseconds_to_seconds(dur), wid, font, min_gap
        )
        # Calculate the height of the text
        font_height = painter.fontMetrics().height()
        line_height = 5
        y = self.rect().height()

        for p in loc:

            i = seconds_to_milliseconds(p[0] * wid / dur)

            # Calculate the position of the text
            text_width = fm.boundingRect(p[1]).width()
            text_position = QPointF(i - text_width / 2, font_height)

            # Draw the text
            painter.drawText(text_position, p[1])

            # Calculate the position of the line
            painter.drawLine(QPointF(i, y), QPointF(i, y - line_height))


class Annotation(QGraphicsRectItem):
    DEFAULT_PEN_COLOR = QColor(0, 0, 0, 255)
    DEFAULT_BG_COLOR = QColor(255, 48, 48, 128)
    DEFAULT_FONT_COLOR = QColor(0, 0, 0, 255)

    def __init__(
        self,
        timeline_widget: TimeLineWidget = None,
        timelineLine=None,
        lower_bound: int = None,
        upper_bound: int = None,
    ):
        """Initializes the Annotation widget"""
        super().__init__(timelineLine)
        self.brushColor = self.DEFAULT_BG_COLOR
        self.penColor = self.DEFAULT_PEN_COLOR
        self.fontColor = self.DEFAULT_FONT_COLOR
        self.group = None
        self.name = None
        self.timelineWidget = timeline_widget
        self.startTime = timeline_widget.value
        self.endTime = timeline_widget.value
        self.timeline_line: TimelineLine = timelineLine
        self.startXPosition = int(
            self.startTime
            * self.timelineWidget.scene.width()
            / self.timelineWidget.duration
        )
        self.endXPosition = self.startXPosition
        self.set_default_rect()
        self.selected = False
        self.startHandle: AnnotationHandle = None
        self.endHandle: AnnotationHandle = None

        self.setX(self.startXPosition)
        self.setY(TimelineLineLabel.FIXED_HEIGHT)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    @staticmethod
    def annotationDrawCanBeInitiate(annotations, value):
        """Check if the annotation can be initiated"""
        lower_bound = upper_bound = None
        valid = True

        # Loop through the annotations of the selected timeline line
        for a in annotations:
            if a.startTime <= value <= a.endTime:
                valid = False
                break
            if not lower_bound:
                if a.endTime < value:
                    lower_bound = a.endTime
            else:
                if a.endTime < value:
                    if lower_bound < a.endTime:
                        lower_bound = a.endTime
            if not upper_bound:
                if a.startTime > value:
                    upper_bound = a.startTime
            else:
                if a.startTime > value:
                    if upper_bound > a.startTime:
                        upper_bound = a.startTime
        return valid, lower_bound, upper_bound

    def set_default_rect(self):
        self.setRect(
            QRectF(
                0,
                0,
                self.endXPosition - self.startXPosition,
                TimelineLine.FIXED_HEIGHT - TimelineLineLabel.FIXED_HEIGHT,
            )
        )

    def mousePressEvent(self, event):
        return

    def mouseReleaseEvent(self, event):
        return

    def mouseDoubleClickEvent(self, event):
        if not self.timelineWidget.currentAnnotation:
            self.setSelected(True)
            self.calculateBounds()

    def focusOutEvent(self, event):
        self.setSelected(False)
        super().focusOutEvent(event)

    def contextMenuEvent(self, event):
        if not self.isSelected():
            super().contextMenuEvent(event)
            return
        menu = QMenu()
        menu.addAction("Delete").triggered.connect(self.on_remove)
        menu.exec(event.screenPos())

    def on_remove(self):
        self.remove()

    def remove(self):
        self.timelineWidget.scene.removeItem(self)
        if self in self.timeline_line.annotations:
            self.timeline_line.remove_annotation(self)
        if self.group:
            self.group.remove_annotation(self)
        del self

    def paint(self, painter, option, widget=...):
        # Draw the annotation rectangle
        self._draw_rect(painter)

        # Draw the name of the annotation in the annotation rectangle
        self._draw_name(painter)

        if self.isSelected():
            self.show_handles()
        else:
            self.hide_handles()

    def _draw_rect(self, painter):
        """Draw the annotation rectangle"""
        pen: QPen = QPen(self.penColor)

        if self.isSelected():
            # Set border dotline if annotation is selected
            pen.setStyle(Qt.PenStyle.DotLine)
        painter.setPen(pen)
        painter.setBrush(self.brushColor)

        # Draw the rectangle
        painter.drawRect(self.rect())

    def _draw_name(self, painter):
        """Draws the name of the annotation"""
        if self.name:
            if colour.Color(self.brushColor.name()).luminance < 0.5:
                col = Qt.GlobalColor.white
            else:
                col = Qt.GlobalColor.black
            painter.setPen(col)
            painter.setBrush(col)
            painter.drawText(
                self.rect(), Qt.AlignmentFlag.AlignCenter, self.name
            )

    def set_group(self, group=None):
        """Updates the group"""
        if group is None:
            self.group = None
            self.brushColor = self.DEFAULT_BG_COLOR
        else:
            self.group = group
            self.brushColor = group.color
            if self.name is None:
                self.name = group.name
            self.setToolTip(self.name)

    def update_rect(self, new_rect: QRectF = None):
        new_rect = new_rect or self.timelineWidget.scene.sceneRect()
        # Calculate position to determine width
        self.startXPosition = (
            self.startTime * new_rect.width() / self.timelineWidget.duration
        )
        self.endXPosition = (
            self.endTime * new_rect.width() / self.timelineWidget.duration
        )
        self.setX(self.startXPosition)

        # Update the rectangle
        rect = self.rect()
        rect.setWidth(self.endXPosition - self.startXPosition)
        self.setRect(rect)

        if self.startHandle:
            self.startHandle.setX(self.rect().x())
            self.endHandle.setX(self.rect().width())

    def update_start_time(self, startTime: int):
        self.startTime = startTime
        self.update_rect()
        self.update()

    def update_end_time(self, endTime: int):
        """Updates the end time"""
        self.endTime = endTime
        self.update_rect()
        self.update()

    def update_selectable_flags(self):
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.update()

    def create_handles(self):
        self.startHandle = AnnotationStartHandle(self)
        self.endHandle = AnnotationEndHandle(self)

    def ends_creation(self):
        """Ends the creation of the annotation"""
        self.update_selectable_flags()
        self.create_handles()

        # if startTime is greater than endTime then swap times
        if self.startTime > self.endTime:
            self.startTime, self.endTime = self.endTime, self.startTime
            self.update_rect()

        # Add this annotation to the annotation list of the timeline line
        self.timeline_line.add_annotation(self)

        self.update()

    def show_handles(self):
        if self.startHandle:
            self.startHandle.setVisible(True)
        if self.endHandle:
            self.endHandle.setVisible(True)

    def hide_handles(self):
        if self.startHandle:
            self.startHandle.setVisible(False)
        if self.endHandle:
            self.endHandle.setVisible(False)

    def calculateBounds(self):
        _, lower_bound, upper_bound = Annotation.annotationDrawCanBeInitiate(
            list(filter(lambda x: x != self, self.timeline_line.annotations)),
            self.startTime,
        )
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def get_time_from_bounding_box(self, time) -> int:
        if self.lower_bound and time < self.lower_bound:
            time = self.lower_bound
        elif self.upper_bound and time > self.upper_bound:
            time = self.upper_bound
        return time


class AnnotationHandle(QGraphicsRectItem):
    def __init__(self, annotation: Annotation, value: int, x: float):
        super().__init__(annotation)
        self.annotation = annotation
        self.value = value

        self.setPen(self.annotation.penColor)
        self.setBrush(self.annotation.brushColor)
        self.setVisible(False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setAcceptDrops(True)

        width = 9
        self._height = annotation.rect().height() / 2
        self.setRect(QRectF(-4.5, 0, width, self._height))

        self.setX(x)
        self.setY(self._height / 2)

    @abstractmethod
    def change_time(self, new_time):
        self.value = new_time

    def focusInEvent(self, event):
        self.annotation.setSelected(True)
        self.annotation.timelineWidget.player.set_position(self.value)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.annotation.setSelected(False)
        super().focusOutEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.setY(self._height / 2)

            # A la souris on déplace le X, il faut changer le temps
            time = int(
                event.scenePos().x()
                * self.annotation.timelineWidget.duration
                / self.annotation.timelineWidget.scene.width()
            )

            time = self.annotation.get_time_from_bounding_box(time)

            self.annotation.timelineWidget.player.set_position(time)


class AnnotationStartHandle(AnnotationHandle):

    def __init__(self, annotation: Annotation):
        super().__init__(annotation, annotation.startTime, 0)

    def change_time(self, time):
        super().change_time(time)
        self.annotation.update_start_time(time)


class AnnotationEndHandle(AnnotationHandle):
    def __init__(self, annotation: Annotation):
        super().__init__(
            annotation, annotation.endTime, annotation.rect().width()
        )

    def change_time(self, time):
        super().change_time(time)
        self.annotation.update_end_time(time)


class AnnotationGroup:
    def __init__(
        self,
        id: int,
        name: str,
        color: QColor = None,
        timeline_line: TimelineLine = None,
    ):
        """Initializes the annotation group"""
        self.id = id
        self.name = name
        self.color = color
        self.timeline_line = timeline_line
        self.annotations = []

    def add_annotation(self, annotation: Annotation):
        annotation.name = self.name
        annotation.set_group(self)
        self.annotations.append(annotation)
        self.annotations.sort(key=lambda x: x.startTime)

    def remove_annotation(self, annotation: Annotation):
        annotation.name = None
        annotation.set_group(None)
        self.annotations.remove(annotation)


class AnnotationGroupDialog(QDialog):
    DEFAULT_COLOR = QColor(255, 255, 255)
    """Dialog to select or create a new annotation group"""

    def __init__(self, timeline_line: TimelineLine = None):
        super().__init__(timeline_line.timelineWidget)
        self.setWindowTitle("New annotation")

        self.color = self.DEFAULT_COLOR
        self.combo_box = QComboBox()
        for group in timeline_line.groups:
            self.combo_box.addItem(group.name, group)
        self.combo_box.setEditable(True)

        self.label_2 = QLabel("New label")
        self.group_name_text = QLineEdit()

        self.button_color_2 = QPushButton("Color")
        self.button_color_2.clicked.connect(self.on_button_color_2_clicked)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.abort_button = QPushButton("Abort")
        self.abort_button.clicked.connect(self.abort)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.accept)

        # Create layout for contents
        layout = QHBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label_2)
        layout.addWidget(self.group_name_text)
        layout.addWidget(self.button_color_2)

        # Create layout for main buttons
        main_button_layout = QHBoxLayout()
        main_button_layout.addWidget(self.cancel_button)
        main_button_layout.addWidget(self.abort_button)
        main_button_layout.addWidget(self.save_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(main_button_layout)

        self.setLayout(main_layout)

        if timeline_line.groups:
            self.state = "choose"
        else:
            self.state = "create"

        self.set_visibility()

    def accept(self):
        if self.combo_box.currentData() or self.state == "create":
            super().accept()
        else:
            self.state = "create"
            self.group_name_text.setText(self.combo_box.currentText())
            self.set_visibility()
            self.group_name_text.setFocus()

    def abort(self):
        confirm_box = AnnotationConfirmMessageBox(self)
        if confirm_box.result() == QMessageBox.DialogCode.Accepted:
            self.done(AnnotationDialogCode.Aborted)

    def on_button_color_2_clicked(self):
        dialog = QColorDialog(self.color, self)
        dialog.exec()
        if dialog.result() == dialog.DialogCode.Accepted:
            self.color = dialog.currentColor()

    def set_visibility(self):
        if self.state == "choose":
            self.combo_box.setVisible(True)
            self.label_2.setVisible(False)
            self.group_name_text.setVisible(False)
            self.button_color_2.setVisible(False)
        else:
            self.combo_box.setVisible(False)
            self.label_2.setVisible(True)
            self.group_name_text.setVisible(True)
            self.button_color_2.setVisible(True)
        self.save_button.setDefault(True)


class AnnotationConfirmMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(
            QMessageBox.Icon.Warning,
            "Warning",
            "Are you sure to abort the creation of this annotation ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            parent,
        )

        self.button(QMessageBox.StandardButton.Yes).clicked.connect(self.accept)
        self.button(QMessageBox.StandardButton.No).clicked.connect(self.reject)
        self.exec()


class AnnotationDialogCode(IntEnum):
    Accepted: int = QDialog.DialogCode.Accepted  # 0
    Canceled: int = QDialog.DialogCode.Rejected  # 1
    Aborted: int = 2
