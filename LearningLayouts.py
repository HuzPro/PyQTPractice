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

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()

        redWidget = Color("#ff6767")
        greenWidget = Color("#54e95c")
        blueWidget = Color("#54bae9")
        purpleWidget = Color("#cb54e9")
        
        layout2.addWidget(redWidget) #light red
        layout2.addWidget(greenWidget)
        layout2.addWidget(blueWidget)
        layout2.addWidget(purpleWidget)

        widget = QWidget()
        widget.setLayout(layout2)
        
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
