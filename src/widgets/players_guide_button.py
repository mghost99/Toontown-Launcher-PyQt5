from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl, QSize
import webbrowser


class PlayersGuide(QPushButton):
    def __init__(self, parent=None, url=None):
        super(PlayersGuide, self).__init__(parent)

        # Setting the size of the button
        self.setFixedSize(122, 38)

        # Positioning the button
        self.move(132, 460)

        # Storing the URL
        self.url = url

        self.default_icon = QIcon("assets/buttons/FAQ1U.png")
        self.hover_icon = QIcon("assets/buttons/FAQ1R.png")  # Rollover (Hover)
        self.pressed_icon = QIcon("assets/buttons/FAQ1D.png")  # Down
        self.disabled_icon = QIcon(
            "assets/buttons/FAQ1G.png")  # Disabled (Greyed)

        # Setting the icon for the button
        self.setIcon(self.default_icon)
        self.setIconSize(QSize(122, 38))  # Setting the size of the icon

        # Connecting the button to the open_url method
        self.clicked.connect(self.open_url)

        # Enabling mouse tracking to detect hover events
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.setIcon(self.hover_icon)

    def leaveEvent(self, event):
        self.setIcon(self.default_icon)

    def mousePressEvent(self, event):
        """Change the icon when the button is pressed."""
        if event.button() == Qt.LeftButton:
            self.setIcon(self.pressed_icon)
        super(PlayersGuide, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setIcon(self.hover_icon)
        super(PlayersGuide, self).mouseReleaseEvent(event)

    def setEnabled(self, enabled):
        super(PlayersGuide, self).setEnabled(enabled)
        if not enabled:
            self.setIcon(self.disabled_icon)
        else:
            self.setIcon(self.default_icon)

    def open_url(self):
        webbrowser.open(self.url)