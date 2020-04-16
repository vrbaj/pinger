import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # set default values and define content

        self.setWindowTitle("Machines monitor")
        self.setMinimumSize(QSize(900, 600))

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence("Alt+Q"))
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Application initialized")



if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Execute application
    sys.exit(app.exec_())