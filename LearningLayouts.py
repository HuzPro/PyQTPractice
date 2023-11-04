from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
import ctypes

# This code makes it so windows doesn't think Pythonw.exe's icon should be used for this window's icon
myappid = u'mycompany.myproduct.subproduct.version' #arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):                              #<- Boilerplate
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)   #<- till here

        self.setWindowIcon(QIcon("icons\\Icon.png"))        #assigning the application/window an icon for the taskbar and window
        self.setWindowTitle("Learning Layouts")            
        self.setMinimumSize(QSize(400, 250))                #setting a minimum size for the window (can't make it smaller)

        self.input = QLineEdit()
        self.label = QLabel()

        self.label.setWordWrap(True)
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])  #initializing the application

window = MainWindow()
window.show()           #Windows are made invisible by default, need show func to show them

app.exec()             #executing the program