import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ctypes

# This code makes it so windows doesn't think Pythonw.exe's icon should be used for this window's icon
myappid = u'mycompany.myproduct.subproduct.version' #arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):                              #<- Boilerplate
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)   #<- till here

        self.setWindowIcon(QIcon("icons\\Icon.png"))        #assigning the application/window an icon for the taskbar and window
        self.setWindowTitle("Mouse Events")            
        self.setMinimumSize(QSize(720, 480))                #setting a minimum size for the window (can't make it smaller)

        self.label = QLabel("Click in this window")         #putting text in middle of screen
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.font = self.label.font()                       #increasing the text size and making it bold using setFont()
        self.font.setPointSize(18)
        self.font.setBold(True)
        self.label.setFont(self.font)

        self.timer = QTimer()
        
        self.setCentralWidget(self.label)


    def mouseMoveEvent(self, e):
        self.label.setText("Oooo moving your mouse...\nnaughty naughty...")
        self.label.setStyleSheet("color:blue")

        if self.timer.isActive():               #deactivating the timer if mouse is not idle
            self.timer.stop()

    def mousePressEvent(self, e):
        self.label.setText("Hello i am pressing my mouse, here too much raining\nOOoooUUuuuOOoooo")
        self.label.setStyleSheet("color:purple")

        if self.timer.isActive():               #deactivating the timer if mouse is not idle
            self.timer.stop()

    def mouseReleaseEvent(self, e):
        self.label.setText("UNHAND ME YOU FIEND")
        self.label.setStyleSheet("color:red")

        self.timer.setInterval(3000)                #Setting a timer to only time out when mouse has been released
        self.timer.timeout.connect(self.resetWindow)#(when the mouse is sitting idle)
        self.timer.start()

    def mouseDoubleClickEvent(self, e):
        self.label.setText("Oh my.. GAAAAAAHHHHHHH u press me 2 tems")
        self.label.setStyleSheet("color:green")

        if self.timer.isActive():               #deactivating the timer if mouse is not idle
            self.timer.stop()

    def resetWindow(self):
        self.label.setText("Click in this window")
        self.label.setStyleSheet("color:black")



app = QApplication([])  #initializing the application

window = MainWindow()
window.show()           #Windows are made invisible by default, need show func to show them

app.exec_()             #executing the program