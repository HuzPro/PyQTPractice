from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from ctypes import windll

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class customDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO! IT'S A DIALOG WINDOW")

        Qbtns = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(Qbtns)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("uhhhh idk i think something happened")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

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

        dlg = customDialog()
        if dlg.exec():
            print("It worked!")
        else:
            print("It didn't work :(")



app = QApplication([])

window = MainWindow()
window.show()

app.exec()