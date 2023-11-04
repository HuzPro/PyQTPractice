from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt6.QtCore import Qt, QSize
import ctypes

# This code makes it so windows doesn't think Pythonw.exe's icon should be used for this window's icon
myappid = u'mycompany.myproduct.subproduct.version' #arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):  #Boilerplate
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowIcon(QIcon("icons\\Icon.png"))
        self.setWindowTitle("Basic Application")
        self.setMinimumSize(QSize(450, 300))

        label = QLabel("Lable with some text in it, cool!")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setCentralWidget(label)
        

app = QApplication([])

window = MainWindow()
window.show()       #Windows are made invisible by default, need show func to show them

app.exec()