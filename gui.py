import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QPushButton, QInputDialog, QLineEdit, QListView
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QSize, pyqtSlot
import PyQt5.QtCore
import PyQt5.QtGui
import worker


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # define system variables?
        self.cluster_list = []
        self.machine_list = {}


        # Main window properties
        self.setWindowTitle("Machines monitor")
        self.setMinimumSize(QSize(900, 600))

        # define Main window items
        # menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        # status bar
        self.status = self.statusBar()
        # buttons
        self.add_cluster_button = QPushButton("Add new cluster", self)

        # list of clusters
        self.cluster_list_view = QListView(self)
        self.init_ui()

    def init_ui(self):
        # set properties of Main Window items
        # set Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence("Alt+Q"))
        exit_action.triggered.connect(self.close)

        # Menu - a little bit useless now
        self.file_menu.addAction(exit_action)

        # Status Bar - for results of reading configuration, saving, some error etc.
        self.status.showMessage("Application initialized")

        # PushButton for adding clusters
        self.add_cluster_button.setToolTip("Click to add new cluster")
        self.add_cluster_button.setGeometry(PyQt5.QtCore.QRect(310, 20, 100, 50))#move(100, 70)
        self.add_cluster_button.clicked.connect(self.add_cluster_click)

        # list for clusters
        self.cluster_list_view.setGeometry(PyQt5.QtCore.QRect(10, 20, 300, 300))
        self.cluster_list_view.setModel(self.cluster_list)


    @pyqtSlot(name="add_cluster_click")
    def add_cluster_click(self):
        cluster_name, ok_pressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if ok_pressed and cluster_name != "":
            worker.add_cluster(cluster_name, self.cluster_list)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Execute application
    sys.exit(app.exec_())