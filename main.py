from playsound import playsound
import threading
import sys
from PyQt5 import QtWidgets
import desigh.Drumpads as design
class ExampleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click0)
        self.pushButton_2.clicked.connect(self.click1)
        self.pushButton_3.clicked.connect(self.click2)
        self.pushButton_5.clicked.connect(self.click3)
        self.pushButton_6.clicked.connect(self.click4)



    def click0(self):
        threading.Thread(target=self.sound0, args=()).start()
    def sound0(self):
        playsound('sounds/36[kb]snare2.aif.mp3')
    def click1(self):
        threading.Thread(target=self.sound1, args=()).start()
    def sound1(self):
        playsound('sounds/24[kb]R8-Snare-5.aif.mp3')
    def click2(self):
        threading.Thread(target=self.sound2, args=()).start()
    def sound2(self):
        playsound('sounds/6[kb]R8-808-1.aif.mp3')
    def click3(self):
        threading.Thread(target=self.sound3, args=()).start()
    def sound3(self):
        playsound('sounds/5[kb]SynDr025.WAV.mp3')
    def click4(self):
        threading.Thread(target=self.sound4, args=()).start()
    def sound4(self):
        playsound('sounds/117[kb]R8-Ride.aif.mp3')




app=QtWidgets.QApplication(sys.argv)
window=ExampleApp()
window.show()
app.exec_()