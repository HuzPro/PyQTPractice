from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from ctypes import windll
from random import choice

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class customDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)    # important to put parent in __init__()
                                    # to tell our custom dialog that it's a child of it's parent window

        self.setWindowTitle("Custom Dialog Box!")

        Qbtns = QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No

        self.buttonBox = QDialogButtonBox(Qbtns)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Uhhhhhh idk, did think something happen?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Dialogs")
        self.setMinimumSize(QSize(350,420))
        self.setWindowIcon(QIcon("icons//Icon.png"))

        buttonsd = QPushButton("Simple Dialog")
        buttonsd.clicked.connect(self.simpleDialogButtonClicked)
        buttonsd.setFixedSize(QSize(160,25))

        buttoncdb = QPushButton("Custom Dialog Box")
        buttoncdb.clicked.connect(self.dialogBoxButtonClicked)
        buttoncdb.setFixedSize(QSize(160,25))

        buttonqdb = QPushButton("Question Dialog Box")
        buttonqdb.clicked.connect(self.questionDialogBoxClicked)
        buttonqdb.setFixedSize(QSize(160,25))

        buttonidb = QPushButton("Informational Dialog Box")
        buttonidb.clicked.connect(self.informationDialogBoxClicked)
        buttonidb.setFixedSize(QSize(160,25))
        
        buttonwdb = QPushButton("Warning Dialog Box")
        buttonwdb.clicked.connect(self.warningDialogBoxClicked)
        buttonwdb.setFixedSize(QSize(160,25))

        buttoncrdb = QPushButton("Critical Dialog Box")
        buttoncrdb.clicked.connect(self.critialDialogBoxClicked)
        buttoncrdb.setFixedSize(QSize(160,25))

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 50, 30, 75)
        layout.addWidget(buttonsd, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(buttoncdb, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(buttonqdb, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(buttonidb, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(buttonwdb, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(buttoncrdb, alignment=Qt.AlignmentFlag.AlignHCenter)

        layoutContainer = QWidget()
        layoutContainer.setLayout(layout)
        
        self.setCentralWidget(layoutContainer)
    
    def critialDialogBoxClicked(self):
        print("Critical Dialog Box Button Pressed")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("WARNING!!!!")
        dlg.setText("THIS PROGRAM IS OFFICIALLY WAY TOO COOL!!!")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.YesToAll)
        dlg.setIcon(QMessageBox.Icon.Critical)
        button = dlg.exec()

        if(button == QMessageBox.StandardButton.Ok):
            print("Okay, Good >_>")
        elif(button == QMessageBox.StandardButton.Yes):
            print("Yes, very good")
        elif(button == QMessageBox.StandardButton.YesToAll):
            print("Glad we agree!")
        else:
            print("wtf amigo...")

    def warningDialogBoxClicked(self):
        print("Warning Dialog Box Button Pressed")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Warning!")
        dlg.setText("This program is getting way too cool!")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes)
        dlg.setIcon(QMessageBox.Icon.Warning)
        button = dlg.exec()

        if(button == QMessageBox.StandardButton.Yes):
            print("Yup!")
        else:
            print("Heeeyyyy! >:(")


    def informationDialogBoxClicked(self):
        print("Information Dialog Box Button Pressed")

        listOfCoolThings = [
            "QCoreApplication handles events even before a main window is created.",
            "QSignalMapper simplifies connecting multiple signals to the same slot.",
            "QThread allows background tasks without blocking the UI.",
            "QThread.connectSignalsAutomatically() simplifies inter-thread communication.",
            "QMimeData enables drag-and-drop functionality across applications.",
            "QStyle`s customize widget appearances across platforms.",
            "QAction`s decouple menu/toolbar actions from specific widgets.",
            "QModel`s power diverse data displays like tables and lists.",
            "QAbstractItemModel`s allow custom data representations and sorting.",
            "QGraphicsView`s offer powerful 2D scene/item management.",
            "QCustomEvent`s enable sending custom data through events.",
            "Qt Designer builds UIs visually and generates Python code.",
            "QMainWindow`s provide a common layout for window applications.",
            "Decorator patterns can enhance signal/slot connections.",
            "PySide2`s commercial license removes PyQt's open-source restrictions.",
            "Qt Quick`s declarative UI language streamlines development.",
            "Model-View-Delegate architecture promotes data separation and flexibility.",
            "Thread pools manage multiple background tasks efficiently.",
            "Signals and slots offer a powerful asynchronous communication mechanism.",
            "PyQt community offers extensive documentation, tutorials, and support.",
            "Qt Stylesheets (CSS-like) allow dynamic UI customization without subclassing.",
            "Qt WebChannel bridges Python and JavaScript for interacting with web content.",
            "QGraphicsEffect`s create visual effects like shadows and transparency.",
            "QAnimation`s add dynamic transitions and interactivity.",
            "Qt Charts` offer various chart types for data visualization.",
            "Model-View-Delegate patterns can be customized for complex data representations.",
            "Qt State Machine`s handle complex UI behavior with finite state transitions.",
            "Designer plugins extend Qt Designer functionality for custom widgets and behaviors.",
            "PyQt bindings for external libraries like OpenCV and NumPy expand functionality.",
            "Testing frameworks like PySide Unittest facilitate robust UI testing.",
            "Qt's built-in accessibility features ensure your app caters to diverse users.",
            "QOpenGLWidget and QOpenGLFramebufferObject unlock hardware-accelerated graphics.",
            "Custom QStyle implementations provide complete control over widget visuals.",
            "Model/View framework supports hierarchical data structures for nested displays.",
            "Multi-threading considerations: QMutex and QWaitCondition for safe resource access.",
            "Qt's internationalization (i18n) support adapts your app to different languages.",
            "Qt Concurrent programming tools like QFuture and QThreadPool for parallel processing.",
            "Decorator patterns for signals and slots can enhance connection behavior.",
            "Qt's built-in debugging tools simplify issue identification and resolution.",
            "PyQt libraries like PyQtGraph and PyQtCharting offer advanced data visualization tools.",
            "Qt's touch screen support caters to modern mobile and embedded devices.",
            "Qt Network module facilitates various network communication protocols.",
            "Qt's built-in printing framework simplifies document generation and printing.",
            "Qt's scripting support allows Python scripting of Qt applications.",
            "Qt's rich multimedia capabilities handle audio, video, and camera input.",
            "Qt's licensing flexibility offers options for open-source and commercial projects.",
            "Qt's active community and extensive documentation provide constant learning resources.",
            "Qt's continuous development ensures access to new features and bug fixes.",
            "PyQt's integration with other Python libraries opens up endless possibilities.",
            "Qt's scalability and performance make it suitable for both small and large projects."
        ]

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Wanna know something cool?")
        dlg.setText(choice(listOfCoolThings))
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()

        if(button == QMessageBox.StandardButton.Ok):
            print("Okay, Cool fact!")
        else:
            print("Boring.")

    def questionDialogBoxClicked(self):
        print("Question Dialog Box Button Pressed")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Riddle me this...")
        dlg.setText("Is this a queston dialog box?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if(button == QMessageBox.StandardButton.Yes):
            print("Yeeaahh!!!")
        else:
            print("Nou ._.")

    def simpleDialogButtonClicked(self):
        print("Simple Dialog Box Button Pressed")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Yo check this out")
        dlg.setText("This is a simple dialog box!")
        button = dlg.exec()

        if(button == QMessageBox.StandardButton.Ok):
            print("Ooookaaaaayy....")

    def dialogBoxButtonClicked(self):
        print("Dialog Box Button Pressed")

        dlg = customDialog(self)
        if dlg.exec():
            print("Yeeee!!!")
        else:
            print("No..? Why... :(")



app = QApplication([])

window = MainWindow()
window.show()

app.exec()
