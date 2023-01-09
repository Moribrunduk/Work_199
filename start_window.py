import sys
import os
import time
import configparser
from PyQt5.QtWidgets import QWidget, QApplication,QLabel,QGridLayout,QPushButton,QVBoxLayout,QLineEdit,QHBoxLayout
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt, QTimer 
sys.path.insert(1,"Bin")

from Bin.Content import MAIN_WINDOW
from Bin.Create_settings_defoult_file import CREATE_SETTINGS_DEFAULT


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
        self.AV = Avtorisation_widow()
        self.AV.show()

class Avtorisation_widow(QWidget):
    def __init__(self):
        super(Avtorisation_widow,self).__init__()
        self.initUI()
    
        
    def initUI(self):
        
        self.layout = QGridLayout()
        self.setWindowTitle("Авторизация")
        self.label_name = QLabel("Имя")
        self.label_password = QLabel("Пароль")
        self.text_name = QLineEdit()
        self.text_password = QLineEdit()
        self.button_ok = QPushButton("ОК")

        self.button_ok.clicked.connect(self.start)

        self.button_exit = QPushButton("Выход")
        self.button_exit.clicked.connect(self.exit_prog)

        self.layout.addWidget(self.label_name,0,0,1,4)
        self.layout.addWidget(self.label_password,1,0,1,4)

        self.layout.addWidget(self.text_name,0,1,1,4)
        self.layout.addWidget(self.text_password,1,1,1,4)

        self.layout.addWidget(self.button_ok,2,3,1,1)
        self.layout.addWidget(self.button_exit,2,4,1,1)

        self.setFixedSize(300,110)
        self.setLayout(self.layout)
        self.show()
    

    def exit_prog(self):
        sys.exit()
    
    def start(self):
            
            self.main_window()
    def main_window(self):

            self.cont = MAIN_WINDOW()
            self.close()
            # TODO
        # except KeyError:
        #     CSD = CREATE_SETTINGS_DEFAULT()
        #     CSD.main()
    # def create_json(self):
    #     CJD = CREATE_JSON_DATA(87100)
    #     CJD.main()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    SP = Start_picture()
    sys.exit(app.exec_())


    