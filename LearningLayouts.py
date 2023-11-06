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

        self.setWindowTitle("Learning Layouts")
        self.setWindowIcon(QIcon("icons\\layout.png"))
        self.setMinimumSize(720,480)

        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        redWidget = Color("#ff6767")
        greenWidget = Color("#54e95c")
        blueWidget = Color("#54bae9")
        purpleWidget = Color("#cb54e9")
        pinkWidget = Color("#e954b7")
        orangeWidget = Color("#f0ad4b")

        layout2.addWidget(redWidget)
        layout2.addWidget(purpleWidget)
        layout2.addWidget(blueWidget)
        
        layout.addLayout(layout2)

        layout.addWidget(greenWidget)

        layout3.addWidget(pinkWidget)
        layout3.addWidget(orangeWidget)

        layout.addLayout(layout3)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)



        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
