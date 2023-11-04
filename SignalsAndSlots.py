from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt6.QtCore import QSize
import ctypes

# This code makes it so windows doesn't think Pythonw.exe's icon should be used for this window's icon
myappid = u'mycompany.myproduct.subproduct.version' #arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):                              #<- Boilerplate
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)   #<- till here

        self.buttonIsChecked = True                         #creating a variable in self
        self.timesclicked = 0

        self.setWindowIcon(QIcon("icons\\Icon.png"))        #assigning the application/window an icon for the taskbar and window
        self.setWindowTitle("Signals and Slots")            
        self.setMinimumSize(QSize(400, 250))                #setting a minimum size for the window (can't make it smaller)

        self.button = QPushButton("Press Me")                    #creates a button widget
        self.button.setCheckable(True)                           #makes the button togglable
        self.button.clicked.connect(self.buttonToggled)          #button click signal is set to "button toggled" function or in pyqt "slot"
        self.button.clicked.connect(self.printButtonClicked)     #prints it was clicked and number of times and if it is toggled or not
        self.button.setChecked(self.buttonIsChecked)             #sets the button's state according to the variable "buttonIsChecked" so when the applications starts for the first time it's already toggled
        
        self.setCentralWidget(self.button)

    
    def printButtonClicked(self):
        print(f"Button was clicked {self.timesclicked} times.", end="\t")
        print("Toggled?", self.buttonIsChecked)

    def buttonToggled(self, checked):
        self.timesclicked += 1
        self.buttonIsChecked = checked

        if self.timesclicked > 10:
            self.button.setText("You've clicked the button way too many times\nIt needs some rest now...")
            self.button.setDisabled(True)
            self.button.setStyleSheet("color : red; background-color : #FF6767; font-size : 12pt; font-weight : bold")
            self.setWindowTitle("Button is angry now")
        



app = QApplication([])  #initializing the application

window = MainWindow()
window.show()           #Windows are made invisible by default, need show func to show them

app.exec()             #executing the program