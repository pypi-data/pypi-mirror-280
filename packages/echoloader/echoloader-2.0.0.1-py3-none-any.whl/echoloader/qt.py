import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow


class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()

        self.browser = QWebEngineView()
        self.profile = QWebEngineProfile('Us2.ai', self.browser)
        self.page = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(self.page)
        self.browser.load(QUrl(sys.argv[1]))
        self.setCentralWidget(self.browser)

        # Set window properties
        self.setWindowTitle("Copilot")
        self.setGeometry(100, 100, 1280, 720)

        self.setWindowIcon(QIcon("assets/logo.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec())
