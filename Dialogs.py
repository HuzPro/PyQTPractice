from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from ctypes import windll

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Dialogs")
        self.setMinimumSize(QSize(600,400))
        self.setWindowIcon(QIcon("icons//Icon.png"))

        button = QPushButton("The Dialog button")
        button.clicked.connect(self.buttonClicked)
        button.setFixedSize(QSize(130,25))
        
        self.setCentralWidget(button)

    def buttonClicked(self, s):
        print(s, "Button Pressed")

        dlg = QDialog(self)
        dlg.setWindowTitle("Dialog Window")
        dlg.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()