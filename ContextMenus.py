from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import ctypes

# This code makes it so windows doesn't think Pythonw.exe's icon should be used for this window's icon
myappid = u'mycompany.myproduct.subproduct.version' #arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):                              #experimenting with different boilerplate
    def __init__(self):
        super().__init__()                                  #till here

        self.setWindowIcon(QIcon("icons\\Icon.png"))        #assigning the application/window an icon for the taskbar and window
        self.setWindowTitle("Context Menus")            
        self.setMinimumSize(QSize(400, 250))                #setting a minimum size for the window (can't make it smaller)

        self.label = QLabel("Right-click literally anywhere on the screen")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setStyleSheet("padding: 30px; font-size: 13pt")

        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = QMenu(self)

        action1 = QAction("test 1", self)
        action1.triggered.connect(self.test1_triggered)
        context.addAction(action1)

        action2 = QAction("test 2", self)
        action2.triggered.connect(self.test2_triggered)
        context.addAction(action2)

        action3 = QAction("test 3", self)
        action3.triggered.connect(self.test3_triggered)
        context.addAction(action3)

        context.exec(e.globalPos())

    def test1_triggered(self):
        print("test1 context menu action clicked")
    
    def test2_triggered(self):
        print("test2 context menu action clicked")

    def test3_triggered(self):
        print("test3 context menu action clicked")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()