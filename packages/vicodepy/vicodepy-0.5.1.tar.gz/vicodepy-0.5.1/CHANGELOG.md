CHANGELOG
=========

0.5.1 - 2024-06-21
------------------

Enhancements:

- The handle for the video player / timeline editor splitter changes now its color when hovered by the mouse
- The title bars of the timelines change color to indicate which one is selected

User-invisible change:

- Code files reorganization

0.5.0 - 2024-06-20
------------------

New features:

- It is now possible to add annotations in multiple timelines
- When clicking on the timeline, the cursor is moved to the mouse position
- It is possible to go forward and backward in time in steps of 5 and 10 frames, either with keystrokes or with buttons in the video player
- Durations of the annotations are now saved in the CSV file
- New system for loading the configuration files (local-, user- and system-wide)
- The program does not exit before proposing to save the created annotations

User-visible fixed bugs:

- During the creation of a new annotation, the other existing annotation can not be made active
- The choice of color for a new label is persistent
- The menu entry for the creation of an annotation is more informative
- The existence of the video file is checked before loading it

0.4.5 - 2024-06-11
------------------

This is a maintenance release. The user visible changes are:

* Require version 6.6.2 of PySide6
* The zooming of the timeline is now centered on the mouse position
* The CSV file is now exported to the same directory where the video file is located
* The annotations appear in chronological order in the exported CSV file
* Improvements in the display of the tick labels in the timescale
* Fix bug when selecting annotations created by pressing the Left key
* At startup, if no video is loaded, a message is shown inviting the user to load a file

0.4.4 - 2024-06-02
------------------

* Annotations do not overlap anymore

0.4.3 - 2024-06-02
------------------

* Use better names for columns in the exported CSV file
* Improved documentation

0.4.2 - 2024-06-01
------------------

* The program accepts now command line arguments
* Annotation labels can be chosen directly using the keyboard, once the annotation dialog is displayed

0.4.1 - 2024-05-31
------------------

* All supported video file formats can now be loaded
* Annotation handles can now be clicked/dragged with the mouse
* Improved color contrast of annotation labels

0.4.0 - 2024-05-30
------------------

* First release to PyPI
* The code has been ported from PQt6 to PySide6
* Bugs fixed / Added features
  - The timeline can be zoomed/dezoomed
  - Annotation creation can be aborted
  - Annotation data can be saved in a CSV file
  - The configuration is now in YAML format and can store several annotation label definitions

0.3.7 - 2024-05-28
------------------

Depend on PySide6

0.3.6 - 2024-05-28
------------------

Add dependency on PyQt6-Qt6

0.3.5 - 2024-05-28
------------------

Force dependency on PyQt6 == 6.4

0.3.4 - 2024-05-23
------------------

Use GitLab CI and AutoPub for automatic publication of the package

0.3.3 - 2024-05-23
------------------

* First release to test.pypi.org
* The timeline is now implemented with QGraphics* objects
* Annotations are now clickable

0.2 - 2024-04-30
----------------

* Fix video playing issues
* The timeline is now functional and it is possible to add annotations

0.1 - 2024-03-25
----------------

Initial release, containing a very simple interface that allows loading a video file and playing it. A timeline is show but is not yet functional.
