from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
import ctypes


# This code makes it so windows doesn't think Pythonw.exe's icon should be used for this window's icon
myappid = u'mycompany.myproduct.subproduct.version' #arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List of Widgets")
        self.setWindowIcon(QIcon("icons\\list.png"))
        self.setMinimumSize(QSize(280, 600))

        layout = QVBoxLayout()

        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        [layout.addWidget(w()) for w in widgets]

        self.windowSizeButton = QPushButton("Print Window's Current Size")
        self.windowSizeButton.clicked.connect(self.WindowSize)
        self.windowSizeButton.setCheckable(True)
        
        layout.addWidget(self.windowSizeButton)

        self.timer = QTimer()

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def WindowSize(self):
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.printWindowSize)
        self.timer.start()

    def printWindowSize(self):
        if self.windowSizeButton.isChecked():
            self.timer.start()
        if self.windowSizeButton.isChecked() != True:
            self.timer.stop()

        print(f"width: {window.size().width()}, height: {window.size().height()}")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
