from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class TQuit(QPushButton):
    def __init__(self, parent=None):
        super(TQuit, self).__init__(parent)

        # Setting the size of the button
        self.setFixedSize(19, 19)

        # Positioning the button
        self.move(710, 1)
        self.default_icon = QIcon("assets/buttons/TQUIT1U.png")
        self.hover_icon = QIcon(
            "assets/buttons/TQUIT1D.png")  # Rollover (Hover)
        self.pressed_icon = QIcon("assets/buttons/TQUIT1D.png")  # Down

        # Setting the icon for the button
        self.setIcon(self.default_icon)
        self.setIconSize(QSize(122, 38))  # Setting the size of the icon

        # Connecting the button to the quit_app method
        self.clicked.connect(self.quit_app)

        # Enabling mouse tracking to detect hover events
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.setIcon(self.hover_icon)

    def leaveEvent(self, event):
        self.setIcon(self.default_icon)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setIcon(self.pressed_icon)
        super(TQuit, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setIcon(self.hover_icon)
        super(TQuit, self).mouseReleaseEvent(event)

    def setEnabled(self, enabled):
        super(TQuit, self).setEnabled(enabled)
        if not enabled:
            self.setIcon(self.disabled_icon)
        else:
            self.hide()

    def quit_app(self):
        # Define what happens when the quit button is clicked
        self.parent().close()