import sys
from PyQt5.QtWidgets import QGridLayout, QLabel,QLineEdit,QPushButton,QWidget, QApplication, QMessageBox
from PyQt5.QtCore import QSettings,QCoreApplication





class AVTORIZATION_WINDOW(QWidget):
    def __init__(self):
        super(AVTORIZATION_WINDOW,self).__init__()
        self.initUI()
        self.Main()
    
        
    def initUI(self):
        
        self.layout = QGridLayout()
        self.setWindowTitle("Авторизация")
        self.label_name = QLabel("Имя")
        self.label_password = QLabel("Пароль")
        self.text_name = QLineEdit()
        self.text_name.setFixedHeight(20)
        self.text_password = QLineEdit()
        self.text_password.setFixedHeight(20)
        
        self.button_ok = QPushButton("ОК")
        self.button_ok.setFixedHeight(20)
        self.button_ok.clicked.connect(self.StartAwtorizationWindow)

        self.button_exit = QPushButton("Выход")
        self.button_exit.setFixedHeight(20)
        self.button_exit.clicked.connect(self.ExitProgramm)

        self.button_new_user = QPushButton("Новый пользователь")
        self.button_new_user.setFixedHeight(20)
        self.button_new_user.clicked.connect(self.NewUser)

        self.layout.addWidget(self.label_name,0,0,1,4)
        self.layout.addWidget(self.label_password,1,0,1,4)

        self.layout.addWidget(self.text_name,0,1,1,4)
        self.layout.addWidget(self.text_password,1,1,1,4)

        self.layout.addWidget(self.button_ok,2,3,1,1)
        self.layout.addWidget(self.button_exit,2,4,1,1)
        self.layout.addWidget(self.button_new_user,3,0,1,5)

        self.setFixedSize(300,130)
        self.setLayout(self.layout)

    def Main(self):

        self.GodVerificztion()
        self.show()
    
    def GodVerificztion(self):
        status = False
        if status == False:
            self.god_verificztion = QLabel("Нет верификации")
            self.layout.addWidget(self.god_verificztion,5,4)
        if status == True:
            self.god_verificztion = QLabel("Верифицировано")
            self.layout.addWidget(self.god_verificztion,5,4)
    
    def StartAwtorizationWindow(self):
        user_name = self.text_name.text()
        password = self.text_password.text()
        print(user_name)
        print(password)

        if user_name == "1" and password == "2":
            print("True")
        else:
            QMessageBox.warning(
                self, 'Ошибка', 'Имя пользователя или пароль неверны')

    def ExitProgramm(self):
        sys.exit()

    def NewUser(self):
        print("создать нового пользователя")
    
class CREATE_NEW_USER(QWidget):
    def __init__(self):
        super(CREATE_NEW_USER,self).__init__()
        self.initUI()

    
    def initUI(self):

        self.layout = QGridLayout()
        self.setWindowTitle("Новый пользователь")
        self.label_name = QLabel("Имя")
        self.label_password = QLabel("Пароль")
        self.text_name = QLineEdit()
        self.text_password = QLineEdit()
        self.text_control_password = QLineEdit()
        
        self.button_ok = QPushButton("ОК")
        self.button_ok.setFixedHeight(20)
        self.button_ok.clicked.connect(self.SaveUserInputLoadAvtorization)

        self.button_exit = QPushButton("Выход")
        self.button_exit.setFixedHeight(20)
        self.button_exit.clicked.connect(self.ExitProgramm)

        self.layout.addWidget(self.label_name,0,0,1,4)
        self.layout.addWidget(self.label_password,1,0,1,4)

        self.layout.addWidget(self.text_name,0,1,1,4)
        self.layout.addWidget(self.text_password,1,1,1,4)
        self.layout.addWidget(self.text_control_password,2,1,1,4)
        
        self.layout.addWidget(self.button_ok,3,3,1,1)
        self.layout.addWidget(self.button_exit,3,4,1,1)
        
        self.setFixedSize(300,200)
        self.setLayout(self.layout)

        self.Qset()
        self.show()

    def Qset(self):
        
        self.settings = QSettings("NITIC")
        self.settings.beginGroup("GOD_parameters")
        self.settings.setValue("Password", "19921128Qe")
        self.settings.endGroup()
        self.settings.beginGroup("Users")
        self.settings.endGroup()


        
    def OutData(self):
        self.settings.beginGroup("GOD_parameters")
        print(self.settings.value("Password"))
        self.settings.endGroup()
        
    
    def SaveUserInputLoadAvtorization(self):

        # ОПЕРАЦИИ С ЛОГИНОМ
        user_name = self.text_name.text()
        self.settings.beginGroup("Users")
        # Проверяем есть ли в реестре такой пользователь
        control_name = self.settings.value(f"{user_name}")
        
        
        if control_name != None:
            QMessageBox.warning(
                self, 'Ошибка', 'Пользователь с таким именем уже существует')
            
        else:
            # Проверяем введенные пароли
            password = self.text_password.text()
            control_password = self.text_control_password.text()
            if password != control_password:
                QMessageBox.warning(
                self, 'Ошибка', 'Пароли не совпадают')
            else:
                self.settings.setValue(user_name,password)
                self.settings.endGroup()
                self.hide()
                self.AW = AVTORIZATION_WINDOW()


    def ShowAvtoriztionWindow(self):
        AW = AVTORIZATION_WINDOW()
        AW.show()

    def ExitProgramm(self):
            sys.exit()



if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    QCoreApplication.setApplicationName("NITIC")
    QCoreApplication.setApplicationName("GOD_PROGRAMM")
    # AW = AVTORIZATION_WINDOW()
    CNU = CREATE_NEW_USER()
    sys.exit(app.exec_())
