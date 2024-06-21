from PySide6.QtWidgets import QDialog, QLineEdit, QFormLayout, QDialogButtonBox

class TimelineLineDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add a new timeline line")

        self.nameLineEdit = QLineEdit(self)
        self.layout = QFormLayout(self)
        self.layout.addRow("Enter name of the new timeline line :", self.nameLineEdit)

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
                                        self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

    def get_text(self):
        return self.nameLineEdit.text()