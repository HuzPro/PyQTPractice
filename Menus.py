from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction, QKeySequence
from PyQt6.QtCore import QSize
from ctypes import windll

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Menus")
        self.setMinimumSize(QSize(600,400))
        self.setWindowIcon(QIcon("icons//drop-down-menu.png"))

        menu = self.menuBar()

        exitProgram = QAction("&Exit", self)
        exitProgram.setShortcut(QKeySequence("Ctrl+e"))
        exitProgram.triggered.connect(exit)

        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(exitProgram)

        print1 = QAction(QIcon("icons//Icon.png"), "&Print 1", self)
        print1.setShortcut(QKeySequence("Ctrl+1"))
        print1.triggered.connect(self.Print1)

        print2 = QAction(QIcon("icons//Icon2.png"), "&Print 2", self)
        print2.setShortcut(QKeySequence("Ctrl+2"))
        print2.triggered.connect(self.Print2)

        runMenu = menu.addMenu("&Run")
        printOptions = runMenu.addMenu("Print Options")
        printOptions.addActions([print1, print2])




    def Print1(self):
        print("Print 1 clicked")

    def Print2(self):
        print("Print 2 clicked")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()