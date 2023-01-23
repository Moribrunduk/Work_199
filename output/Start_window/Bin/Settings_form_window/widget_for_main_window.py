from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

import configparser

settings = configparser.ConfigParser()

settings.read("data\SETTINGS.ini",encoding="utf-8")


class DefectoscopistRGG(QWidget):
    def __init__(self):
        super(DefectoscopistRGG, self).__init__()
        self.initUI()
    def initUI(self):

        # создаем горизонтальную группировку которую вставим в рамку |3 ----
        #                                                            |4 ---- Процент
        #                                                            |5 ---- |30|%

        self.layout_for_settings = QHBoxLayout()
        # правый столбик в настройках
        self.layout_for_procent_in_settings = QVBoxLayout()
        procent_label = QLabel("% оплаты\n от тарифа")
        self.procent_text = QLineEdit(settings["87100"]["procent_text"])
        self.procent_text.setStyleSheet("QLineEdit{font-size: 25px}")
        self.procent_text.setMaximumSize(50,50)
        

        self.layout_for_procent_in_settings.addWidget(procent_label)
        self.layout_for_procent_in_settings.addWidget(self.procent_text)

        # левый столбик в настройках
        self.layout_for_group_cvalification = QGridLayout()

        cv_three = QLabel("    3")
        cv_three.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_three_tarif = QLineEdit(settings["87100"]["cv_three_tarif"])
        self.cv_three_tarif.setMaximumWidth(50)
        
        
        self.layout_for_group_cvalification.addWidget(cv_three,0,0)
        self.layout_for_group_cvalification.addWidget(self.cv_three_tarif,0,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_three_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,0,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_four = QLabel("    4")
        cv_four.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_four_tarif = QLineEdit(settings["87100"]["cv_four_tarif"])
        self.cv_four_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_four,1,0)
        self.layout_for_group_cvalification.addWidget(self.cv_four_tarif,1,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_four_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,1,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_five = QLabel("    5")
        cv_five.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_five_tarif = QLineEdit(settings["87100"]["cv_five_tarif"])
        self.cv_five_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_five,2,0)
        self.layout_for_group_cvalification.addWidget(self.cv_five_tarif,2,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_five_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,2,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_six = QLabel("    6")
        cv_six.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_six_tarif = QLineEdit(settings["87100"]["cv_six_tarif"])
        self.cv_six_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_six,3,0)
        self.layout_for_group_cvalification.addWidget(self.cv_six_tarif,3,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_six_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,3,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)
        
        self.layout_for_settings.addLayout(self.layout_for_group_cvalification)
        self.layout_for_settings.addLayout(self.layout_for_procent_in_settings)


        # создаем группировку в рамке и добавляем туда виджеты
        self.layout_in_frame = QVBoxLayout()
        self.Cvalification_title = QLabel("Разряд")
        self.layout_in_frame.addWidget(self.Cvalification_title)
        self.layout_in_frame.addLayout(self.layout_for_settings)
       
        # создаем рамку в которой будут все виджеты
        self.main_group_box = QGroupBox()
        self.main_group_box.setStyleSheet("QGroupBox{font-size: 12px}")
        self.main_group_box.setTitle("Дефектоскопист РГГ (87100)")
        self.main_group_box.setMaximumWidth(200)
        self.main_group_box.setMaximumHeight(200)
        self.main_group_box.setLayout(self.layout_in_frame)

        # создаем группировку вертикальная
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_group_box)
        
        # присваеваем главному экрану групировку виджетов
        self.setLayout(self.main_layout)
        
class DefectoscopistPZRS(QWidget):
    def __init__(self):
        super(DefectoscopistPZRS, self).__init__()
        self.initUI()

    def initUI(self):

        # создаем горизонтальную группировку которую вставим в рамку |3 ----
        #                                                            |4 ---- Процент
        #                                                            |5 ---- |30|%

        self.layout_for_settings = QHBoxLayout()

        # правый столбик в настройках
        self.layout_for_procent_in_settings = QVBoxLayout()
        procent_label = QLabel("% оплаты\n от тарифа")
        self.procent_text = QLineEdit(settings["87200"]["procent_text"])
        self.procent_text.setStyleSheet("QLineEdit{font-size: 25px}")
        self.procent_text.setMaximumSize(50,50)
        
        self.layout_for_procent_in_settings.addWidget(procent_label)
        self.layout_for_procent_in_settings.addWidget(self.procent_text)

        # левый столбик в настройках
        self.layout_for_group_cvalification = QGridLayout()

        cv_three = QLabel("    3")
        cv_three.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_three_tarif = QLineEdit(settings["87200"]["cv_three_tarif"])
        self.cv_three_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_three,0,0)
        self.layout_for_group_cvalification.addWidget(self.cv_three_tarif,0,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_three_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,0,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_four = QLabel("    4")
        cv_four.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_four_tarif = QLineEdit(settings["87200"]["cv_four_tarif"])
        self.cv_four_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_four,1,0)
        self.layout_for_group_cvalification.addWidget(self.cv_four_tarif,1,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_four_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,1,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_five = QLabel("    5")
        cv_five.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_five_tarif = QLineEdit(settings["87200"]["cv_five_tarif"])
        self.cv_five_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_five,2,0)
        self.layout_for_group_cvalification.addWidget(self.cv_five_tarif,2,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_five_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,2,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_six = QLabel("    6")
        cv_six.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_six_tarif = QLineEdit(settings["87200"]["cv_six_tarif"])
        self.cv_six_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_six,3,0)
        self.layout_for_group_cvalification.addWidget(self.cv_six_tarif,3,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_six_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,3,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)
        
        self.layout_for_settings.addLayout(self.layout_for_group_cvalification)
        self.layout_for_settings.addLayout(self.layout_for_procent_in_settings)

        # создаем группировку в рамке и добавляем туда виджеты
        self.layout_in_frame = QVBoxLayout()
        self.Cvalification_title = QLabel("Разряд")
        self.layout_in_frame.addWidget(self.Cvalification_title)
        self.layout_in_frame.addLayout(self.layout_for_settings)
       
        # создаем рамку в которой будут все виджеты
        self.main_group_box = QGroupBox()
        self.main_group_box.setStyleSheet("QGroupBox{font-size: 12px}")
        self.main_group_box.setTitle("Дефектоскопист ПЗРС (87200)")
        self.main_group_box.setMaximumWidth(200)
        self.main_group_box.setMaximumHeight(200)
        self.main_group_box.setLayout(self.layout_in_frame)

        # создаем группировку вертикальная
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_group_box)
        
        # присваеваем главному экрану групировку виджетов
        self.setLayout(self.main_layout)

class Fotolaborant(QWidget):
    def __init__(self):
        super(Fotolaborant, self).__init__()
        self.initUI()

    def initUI(self):

        # создаем горизонтальную группировку которую вставим в рамку |3 ----
        #                                                            |4 ---- Процент
        #                                                            |5 ---- |30|%

        self.layout_for_settings = QHBoxLayout()

        # правый столбик в настройках
        self.layout_for_procent_in_settings = QVBoxLayout()
        procent_label = QLabel("% оплаты\n от тарифа")
        self.procent_text = QLineEdit(settings["08300"]["procent_text"])
        self.procent_text.setStyleSheet("QLineEdit{font-size: 25px}")
        self.procent_text.setMaximumSize(50,50)
        
        self.layout_for_procent_in_settings.addWidget(procent_label)
        self.layout_for_procent_in_settings.addWidget(self.procent_text)

        # левый столбик в настройках
        self.layout_for_group_cvalification = QGridLayout()

        cv_three = QLabel("    3")
        cv_three.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_three_tarif = QLineEdit(settings["08300"]["cv_three_tarif"])
        self.cv_three_tarif.setMaximumWidth(50)
        
        
        self.layout_for_group_cvalification.addWidget(cv_three,0,0)
        self.layout_for_group_cvalification.addWidget(self.cv_three_tarif,0,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_three_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,0,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_four = QLabel("    4")
        cv_four.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_four_tarif = QLineEdit(settings["08300"]["cv_four_tarif"])
        self.cv_four_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_four,1,0)
        self.layout_for_group_cvalification.addWidget(self.cv_four_tarif,1,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_four_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,1,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_five = QLabel("    5")
        cv_five.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_five_tarif = QLineEdit(settings["08300"]["cv_five_tarif"])
        self.cv_five_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_five,2,0)
        self.layout_for_group_cvalification.addWidget(self.cv_five_tarif,2,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_five_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,2,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)

        cv_six = QLabel("    6")
        cv_six.setMaximumWidth(20)
        rub = QLabel("P")
        self.cv_six_tarif = QLineEdit(settings["08300"]["cv_six_tarif"])
        self.cv_six_tarif.setMaximumWidth(50)
        
        self.layout_for_group_cvalification.addWidget(cv_six,3,0)
        self.layout_for_group_cvalification.addWidget(self.cv_six_tarif,3,1)
        self.layout_for_group_cvalification.setAlignment(self.cv_six_tarif,QtCore.Qt.AlignLeft)
        self.layout_for_group_cvalification.addWidget(rub,3,2)
        self.layout_for_group_cvalification.setAlignment(rub,QtCore.Qt.AlignLeft)
        
        self.layout_for_settings.addLayout(self.layout_for_group_cvalification)
        self.layout_for_settings.addLayout(self.layout_for_procent_in_settings)

        # создаем группировку в рамке и добавляем туда виджеты
        self.layout_in_frame = QVBoxLayout()
        self.Cvalification_title = QLabel("Разряд")
        self.layout_in_frame.addWidget(self.Cvalification_title)
        self.layout_in_frame.addLayout(self.layout_for_settings)
       
        # создаем рамку в которой будут все виджеты
        self.main_group_box = QGroupBox()
        self.main_group_box.setStyleSheet("QGroupBox{font-size: 12px}")
        self.main_group_box.setTitle("Фотолаборант (08300)")
        self.main_group_box.setMaximumWidth(200)
        self.main_group_box.setMaximumHeight(200)
        self.main_group_box.setLayout(self.layout_in_frame)

        # создаем группировку вертикальная
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_group_box)
        
        # присваеваем главному экрану групировку виджетов
        self.setLayout(self.main_layout)

        return self.main_layout

class Form_with_day(QWidget):
    def __init__(self):
        super(Form_with_day, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.main_layout = QGridLayout()
        Title = QLabel("Сокращения в табеле")
        Title.setStyleSheet("font: 15pt Arial")
        Title.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.main_layout.addWidget(Title,0,0,1,4)
        self.main_layout.setAlignment(QtCore.Qt.AlignCenter)
        days_keys = eval(settings["Days"]["days_keys"])
        days_values = eval(settings["Days"]["days_values"])

        dict_days_names = {}
        for i in range(len(days_keys)):
            dict_days_names[days_keys[i]] = days_values[i]

        # dict_days_names = {'"ИО" - ':'И.о.мастера',
        #                     '"О" - ':'Отпуск очередной',
        #                     '"Э" - ':'Отпуск учебный',
        #                     '"Р" - ':'Отпуск по беремености',
        #                     '"А" - ':'Отпуск за свой счет',
        #                     '"Ж" - ':'Пенсионный день/уход за детьми',
        #                     '"Д" - ':'Донорский день',
        #                     '"М" - ':'Медкомиссия',
        #                     '"Б" - ':'Больничный',
        #                     '"К" - ':'Командировка'}

        x = 1
        for key,value in dict_days_names.items():
            label = QLabel(key)
            self.Line = QLineEdit(value)
            self.Line.setMinimumWidth(200)
            self.main_layout.addWidget(label,x,1)
            self.main_layout.addWidget(self.Line,x,2)
            x+=1
        self.setLayout(self.main_layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # DRGG = DefectoscopistRGG()
    # DPZRS =DefectoscopistPZRS()
    # FOTO = Fotolaborant()
    # FRMD = Form_with_day()
    app.exec_()