import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication, QFrame, QPushButton,QLineEdit,QLabel)
from configparser import ConfigParser


from widget_for_main_window import (DefectoscopistRGG , DefectoscopistPZRS, Fotolaborant, Form_with_day)
sys.path.insert(1,"data")




class Settings_window(QWidget):
    
    def __init__(self):
        super(Settings_window,self).__init__()
        self.settings = ConfigParser()
        self.settings.read("data/SETTINGS.ini", encoding="utf-8")
        self.initUI()
        
    # создаем функцию которая переопределяет хозяина виджета
    def DRGG_FUNC(self):
        self.DRGG = DefectoscopistRGG()
        return self.DRGG.main_layout
    
    def DPZRS_FUNC(self):
        self.DPZRS = DefectoscopistPZRS()
        return self.DPZRS.main_layout
    
    def FOTO_FUNC(self):
        self.FOTO = Fotolaborant()
        return self.FOTO.main_layout
    
    def DAYS_FUNC(self):
        self.DAYS = Form_with_day()
        return self.DAYS.main_layout

    def Save_data(self):
        """сохраняем данные введенные пользователем"""
        
        

        self.settings["87100"]["cv_three_tarif"]=self.DRGG.cv_three_tarif.text()
        self.settings["87100"]["cv_four_tarif"]=self.DRGG.cv_four_tarif.text()
        self.settings["87100"]["cv_five_tarif"]=self.DRGG.cv_five_tarif.text()
        self.settings["87100"]["cv_six_tarif"]=self.DRGG.cv_six_tarif.text()
        self.settings["87100"]["procent_text"]=self.DRGG.procent_text.text()
        
        self.settings["87200"]["cv_three_tarif"]=self.DPZRS.cv_three_tarif.text()
        self.settings["87200"]["cv_four_tarif"]=self.DPZRS.cv_four_tarif.text()
        self.settings["87200"]["cv_five_tarif"]=self.DPZRS.cv_five_tarif.text()
        self.settings["87200"]["cv_six_tarif"]=self.DPZRS.cv_six_tarif.text()
        self.settings["87200"]["procent_text"]=self.DPZRS.procent_text.text()

        self.settings["08300"]["cv_three_tarif"]=self.FOTO.cv_three_tarif.text()
        self.settings["08300"]["cv_four_tarif"]=self.FOTO.cv_four_tarif.text()
        self.settings["08300"]["cv_five_tarif"]=self.FOTO.cv_five_tarif.text()
        self.settings["08300"]["cv_six_tarif"]=self.FOTO.cv_six_tarif.text()
        self.settings["08300"]["procent_text"]=self.FOTO.procent_text.text()

        
        # сокращения дней
        # По другому не придумал(начинается с 31.т.к до этого полно всяких лэйблов)
        self.days_keys = [self.label.text() for self.label in self.findChildren(QLabel)]
        

        # расшифровка сокращений дней
        # По другому не придумал(начинается с 15.т.к до этого полно всяких едитов)
        self.days_values = [self.lineEdit.text() for self.lineEdit in self.findChildren(QLineEdit)]
       
        self.settings["Days"]["days_keys"]=str(self.days_keys[31:])
        self.settings["Days"]["days_values"]=str(self.days_values[15:])
        
        print("[INFO] --- save_conpleted --- [INFO]")
        
        with open("data\SETTINGS.ini", "w",encoding="utf-8") as config_file:
            self.settings.write(config_file)

    def initUI(self):

        # создаем рамки
        DRGG = self.DRGG_FUNC()
        self.form_for_rgg = QFrame()
        self.form_for_rgg.setLayout(DRGG)
        
        DPZRS = self.DPZRS_FUNC()
        self.form_for_pzrs = QFrame()
        self.form_for_pzrs.setLayout(DPZRS)
        
        FOTO = self.FOTO_FUNC()
        self.form_for_foto = QFrame()
        self.form_for_foto.setLayout(FOTO)
        DAYS = self.DAYS_FUNC()
        self.form_for_days = QFrame()
        self.form_for_days.setLayout(DAYS)
        # группировка для рамок
        self.layout_for_load_widget = QGridLayout()
        self.layout_for_load_widget.addWidget(self.form_for_rgg,0,0)
        self.layout_for_load_widget.addWidget(self.form_for_pzrs,1,0)
        self.layout_for_load_widget.addWidget(self.form_for_foto,2,0)
        self.layout_for_load_widget.addWidget(self.form_for_days,0,1,3,4)
        self.layout_for_load_widget.setColumnMinimumWidth(1,100)
        self.layout_for_load_widget.setColumnStretch(1,100)
        self.layout_for_load_widget.setAlignment(self.form_for_days,QtCore.Qt.AlignTop)
        # кнопка сохранения
        self.button_save = QPushButton()
        self.button_save.setText("Cохранить")
        self.button_save.clicked.connect(self.Save_data)
        self.layout_for_load_widget.addWidget(self.button_save,2,2)
        # основная группировка
        self.setLayout(self.layout_for_load_widget)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Settings_window()
    w.show()
    sys.exit(app.exec_())