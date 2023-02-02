import sys
import json
import xlwt
import xlrd
from PyQt5.QtWidgets import QWidget, QApplication,QLabel,QGridLayout,QPushButton,QLineEdit,QShortcut
from PyQt5.QtGui import  QPixmap, QKeySequence
from PyQt5.QtCore import Qt, QTimer 
sys.path.insert(1,"Bin")
sys.path.insert(2,"Bin\Avtorization_window")

from Bin.Content import MAIN_WINDOW
from Bin.Create_settings_defoult_file import CREATE_SETTINGS_DEFAULT
from Bin.Avtorization_window.Avtorization_main_window import AVTORIZATION_WINDOW


class Start_picture(QWidget):
    def __init__(self):
        super(Start_picture,self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.setWindowOpacity(0.8)
        self.label = QLabel(self)
        pixmap = QPixmap('Bin\image.jpg')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())  # fit window to the image
        self.version_number = QLabel("VERSION:0.1.1",self)
        self.version_number.setStyleSheet("font: 15pt arial;"
                                           " color: Orange;")
        self.timer_close = QTimer()

        CSD = CREATE_SETTINGS_DEFAULT()
        CSD.main()
        self.timer_close.timeout.connect(self.close)
        self.timer_close.timeout.connect(self.show_avtorisation_widow)
        self.timer_close.start(3000)
        

        self.show()
    
    def show_avtorisation_widow(self):
        self.timer_close.stop()
        self.AW = AVTORIZATION_WINDOW()
        self.AW.show()


    def main_window(self):

            self.cont = MAIN_WINDOW()
            self.close()
            # TODO
           

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    SP = Start_picture()
    sys.exit(app.exec_())


    