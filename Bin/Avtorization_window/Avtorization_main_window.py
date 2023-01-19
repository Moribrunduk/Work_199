import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QGridLayout, QLabel,QLineEdit,QPushButton,QWidget, QApplication, QMessageBox,QShortcut
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
        self.button_ok.clicked.connect(self.Verification)

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

        self.setFixedSize(320,130)
        self.setLayout(self.layout)

    def Main(self):
        self.Qset()
        self.GodVerificztion()
        self.show()
    
    def Qset(self):
        self.settings = QSettings("NITIC")
        self.settings.beginGroup("GOD_parameters")
        self.settings.setValue("Password", "19921128Qe")
        self.settings.endGroup()
    
    
        
    
    def GodVerificztion(self):

        status = False
        if status == False:
            self.god_verificztion = QLabel("Нет верификации")
            self.layout.addWidget(self.god_verificztion,5,4)
        if status == True:
            self.god_verificztion = QLabel("Верифицировано")
            self.layout.addWidget(self.god_verificztion,5,4)
        
        return status
    
    # def on_open(self):
        
    #     self.god_label_password = QLabel("Пароль  ")
    #     self.god_text_password = QLineEdit()
    #     self.god_text_password.setFixedHeight(20)
    #     self.layout.addWidget(self.god_label_password,4,0,1,4)
    #     self.layout.addWidget(self.god_text_password,4,1,1,4)
    #     self.god_ok_button = 
    #     self.setFixedSize(320,155)
    #     print('sdfds')


    
    def Verification(self):
        self.settings.beginGroup("Users")
        
        user_name = self.text_name.text()
        password = self.text_password.text()

        control_name = self.settings.value(f"{user_name}")
        print(control_name)

        if control_name == None:
            QMessageBox.warning(
                self, 'Ошибка', 'Ошибка: такого пользователя не существует')
        elif control_name != password:
            QMessageBox.warning(
                self, 'Ошибка', 'Ошибка: неверный пароль')
        elif self.GodVerificztion() == False:
             QMessageBox.warning(
                self, 'Ошибка', 'Ошибка: Права пользователя не подтверждены')
        else:
            print("удача")

        self.settings.endGroup()
        

    def ExitProgramm(self):
        sys.exit()

    def NewUser(self):
        self.hide()
        self.CNU = CREATE_NEW_USER()
        
    
class CREATE_NEW_USER(QWidget):
    
    def __init__(self):
        super(CREATE_NEW_USER,self).__init__()
        self.initUI()
        self.Main()
    
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
        
        self.setFixedSize(300,150)
        self.setLayout(self.layout)

    def Main(self):
        self.Qset()
        self.HotkeyKeybord()
        self.show()

    def Qset(self):
        self.settings = QSettings("NITIC")

    def HotkeyKeybord(self):
        self.shortcut = QShortcut(QKeySequence("Ctrl+g"), self)
        self.shortcut.activated.connect(self.ShowGodVerification)
    
    def ShowGodVerification(self):
        self.god_label_password = QLabel("Пароль  ")
        self.god_text_password = QLineEdit()
        self.god_text_password.setFixedHeight(20)
        self.layout.addWidget(self.god_label_password,4,0,1,4)
        self.layout.addWidget(self.god_text_password,4,1,1,4)
        self.god_ok_button = QPushButton("Верифицировать")
        self.god_ok_button.clicked.connect(self.ControlPassword)
        self.layout.addWidget(self.god_ok_button,5,0,1,5)
        self.setFixedSize(300,210)
    
   

    def ControlPassword(self):
        self.settings.beginGroup("GOD_parameters")
        god_password_input = self.god_text_password.text()
        print(god_password_input)
        print(self.settings.value("Password"))
        if god_password_input == self.settings.value("Password"):
            self.god_ok_button.setText("Верифицировано")
            self.god_ok_button.setEnabled(False)
        else:
            print("Неверифицирован")
        self.settings.endGroup()
            
        
        
        
        
    
    def SaveUserInputLoadAvtorization(self):
        # ОПЕРАЦИИ С ЛОГИНОМ
        user_name = self.text_name.text()
        self.settings.beginGroup("Users")
        # Проверяем есть ли в реестре такой пользователь
        control_name = self.settings.value(f"{user_name}")
        self.settings.endGroup()
        
        if user_name =="":
            QMessageBox.warning(
                self, 'Ошибка', 'Ошибка: введите имя пользователя')
        elif control_name != None:
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
                try:
                    if self.god_ok_button.text() == "Верифицировано":
                        self.settings.beginGroup("Users")
                        self.settings.setValue(user_name,password)
                        self.settings.endGroup()
                        self.close()
                        self.AW = AVTORIZATION_WINDOW()
                    else:
                        QMessageBox.warning(
                self, 'Ошибка', 'Ошибка: требуется верификация')
                except AttributeError:
                    QMessageBox.warning(
                self, 'Ошибка', 'Ошибка: требуется верификация')

        self.settings.endGroup()


    def ExitProgramm(self):
            sys.exit()



if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    QCoreApplication.setApplicationName("NITIC")
    QCoreApplication.setApplicationName("GOD_PROGRAMM")
    AW = AVTORIZATION_WINDOW()
    # CNU = CREATE_NEW_USER()
    sys.exit(app.exec_())
