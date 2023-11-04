from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from ctypes import windll, cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

myappid = u'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons\\slider.png"))
        self.setWindowTitle("QSlider")
        self.setMinimumSize(QSize(220, 80))

        self.slider = QSlider()

        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setSingleStep(1)
        self.slider.setValue(int(volume.GetMasterVolumeLevelScalar() * 100))
        self.slider.setFixedSize(200,30)


        self.slider.valueChanged.connect(self.sliderValueChanged)
        """ self.slider.sliderMoved.connect(self.sliderPosition)
        self.slider.sliderPressed.connect(self.sliderWasPressed)
        self.slider.sliderReleased.connect(self.sliderWasReleased) """
        
        self.slider.setToolTip(str(self.slider.value()))

        self.volumeLabel = QLabel(f"Volume: {int(volume.GetMasterVolumeLevelScalar() * 100)}%")
        self.volumeLabel.setStyleSheet("margin: 0px, 50px;")
        self.volumeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        

        layout = QGridLayout()
        layout.addWidget(self.volumeLabel, 1, 1)
        layout.addWidget(self.slider, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)



    def sliderValueChanged(self, i):
        self.slider.setToolTip(str(self.slider.value()))
        self.volumeLabel.setText(f"Volume: {str(self.slider.value())}%")
        print(f"Volume: {i}")
        volume.SetMasterVolumeLevelScalar(i / 100, None)
    
    """ def sliderPosition(self, p):
        print(f"Position: {p}")
    
    def sliderWasPressed(self):
        print("Slider Pressed")

    def sliderWasReleased(self):
        print("Slider Released") """

app = QApplication([])

window = MainWindow()
window.show()

app.exec()