from PyQt6.QtWidgets import QMainWindow, QLabel, QToolBar, QApplication, QStatusBar
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QAction
from ctypes import windll

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Toolbars")
        self.setWindowIcon(QIcon("icons//drop-down.png"))
        self.setMinimumSize(QSize(480,300))

        label = QLabel("Test")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        buttonAction = QAction(QIcon("icons//Icon.png"), "&Action Button", self)
        buttonAction.setStatusTip("This is your action button Status tip")
        buttonAction.triggered.connect(self.onMyToolBarButtonClick)
        buttonAction.setCheckable(True)
        toolbar.addAction(buttonAction)

        toolbar.addSeparator()

        buttonAction2 = QAction(QIcon("icons//Icon2.png"),"Action Button 2", self)
        buttonAction2.setStatusTip("This is your action button 2 Status tip")
        buttonAction2.triggered.connect(self.onMyToolBarButtonClick)
        buttonAction2.setCheckable(True)
        toolbar.addAction(buttonAction2)
        
        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("clicked", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()