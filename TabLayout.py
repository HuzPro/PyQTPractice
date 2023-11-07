from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from ctypes import windll

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Tab View")
        self.setWindowIcon(QIcon("icons\\tab.png"))
        self.setMinimumSize(720, 480)

        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stackLayout = QStackedLayout()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addLayout(self.stackLayout)
        
        redButton = QPushButton("Red")
        redButton.pressed.connect(self.activateTab1)
        buttonLayout.addWidget(redButton)
        self.stackLayout.addWidget(Color("red"))

        greenButton = QPushButton("Green")
        greenButton.pressed.connect(self.activateTab2)
        buttonLayout.addWidget(greenButton)
        self.stackLayout.addWidget(Color("green"))

        blueButton = QPushButton("Blue")
        blueButton.pressed.connect(self.activateTab3)
        buttonLayout.addWidget(blueButton)
        self.stackLayout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def activateTab1(self):
        self.stackLayout.setCurrentIndex(0)
    
    def activateTab2(self):
        self.stackLayout.setCurrentIndex(1)

    def activateTab3(self):
        self.stackLayout.setCurrentIndex(2)



app = QApplication([])

window = MainWindow()
window.show()

app.exec()