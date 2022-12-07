import sys
from PyQt5.QtWidgets import QWidget, QApplication,QLabel,QGridLayout,QPushButton,QVBoxLayout,QLineEdit,QHBoxLayout
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt, QTimer 
sys.path.insert(1,"Bin")
from Bin.Content import MAIN_WINDOW


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

        self.setFixedSize(270,110)
        self.setLayout(self.layout)
        self.show()

    def exit_prog(self):
        sys.exit()
    def start(self):
        self.cont = MAIN_WINDOW()
        self.close()

class Change_profession(QWidget):
    def __init__(self):
        super(Change_profession,self).__init__()
        self.initUI()
        
    def initUI(self):

        self.setWindowTitle("Выбор задачи")
        self.main_layout = QVBoxLayout()
        self.DRGG_layout = QHBoxLayout()
        self.buttonDRGG = QPushButton("Распределение премии \n (шифр  №199)")
        self.buttonDRGG.setEnabled()
        self.buttonDRGG.clicked.connect(self.start)
        self.buttonDRGG.setFixedSize(250,80)


        self.layout.addWidget(self.buttonDRGG)
        
        # self.buttonDPZRS = QPushButton("Дефектоскопист ПЗРС\n (87200)")
        # self.buttonDPZRS.clicked.connect(self.start_DPZRS_window)
        # self.buttonDPZRS.setFixedSize(250,80)
        # self.layout.addWidget(self.buttonDPZRS)
        
        # self.buttonFOTO = QPushButton("Фотолаборанты\n (08300)")
        # self.buttonFOTO.clicked.connect((self.start_FOTO_window))
        # self.buttonFOTO.setFixedSize(250,80)
        # self.layout.addWidget(self.buttonFOTO)

        self.setFixedSize(270,100)
        self.setLayout(self.layout)
        self.show()
    
    def start(self):
        self.cont = MAIN_WINDOW()
        self.close()
    # def start_DPZRS_window(self):
    #     pass
    # def start_FOTO_window(self):
    #     pass



    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    SP = Start_picture()
    sys.exit(app.exec_())


    