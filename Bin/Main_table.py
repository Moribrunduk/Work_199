
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QColor
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableView,QApplication,QPushButton,QGridLayout,QMainWindow,QVBoxLayout
import json
import configparser
from collections import Counter

from Create_final_excell_file import CREATE_EXCELL
from Load_file_form import Change_profession


class MAIN_WORK_TABLE(QWidget): 
    
    def __init__(self,proffession_number):
        self.proffession_number = str(proffession_number)
        super(MAIN_WORK_TABLE, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Расчет 199 премии")
        self.resize(500,300)
        self.model = QStandardItemModel()
        self.data_table_view = QTableView()
        self.data_table_view.setModel(self.model)

        self.top_layout = QGridLayout()
        self.main_layout = QVBoxLayout()
        self.Button_layout = QVBoxLayout()

        self.button = QPushButton("Создать файл для печати")
        self.button.clicked.connect(self.ButtonAction)
        self.button2 = QPushButton("Выбрать другой файл")
        self.button2.clicked.connect(self.ButtonActionChangeFile)
        self.button2.clicked.connect(self.ChangeFile)


        self.top_layout.addWidget(self.data_table_view,0,0)
        self.Button_layout.addWidget(self.button)
        self.Button_layout.addWidget(self.button2)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.Button_layout)
        self.setLayout(self.main_layout)

        
        self.save_input_user_for_load_in_file = {}
        self.save_input_user_for_summ_in_file = {}
        
        SETTINGS = configparser.ConfigParser()
        SETTINGS.read("data/SETTINGS.ini", encoding="utf-8")
        current_path = SETTINGS["Settings"][f"current_directory_{self.proffession_number}"]
        with open(f"{current_path}", "r", encoding="utf-8") as file:
             self.all_data = json.load(file)
        self.tabels = self.all_data["шифр"][self.proffession_number]["Табельный"]
        self.add_data()
        self.add_replace_cell()
        self.load_data()
        self.parameters()
        self.summ_pay()
    
    def ButtonAction(self):
        self.CE = CREATE_EXCELL(self.proffession_number)
        self.CE.Main()
    
    def ButtonActionChangeFile(self):
        # SETTINGS = configparser.ConfigParser()
        # SETTINGS.read("data/SETTINGS.ini", encoding="utf-8")
        # SETTINGS["Settings"][f"path_{self.proffession_number}"] = ""
        # SETTINGS["Settings"][f"current_directory_{self.proffession_number}"] = ""
        # with open("data\SETTINGS.ini", "w", encoding="utf-8") as configfile:
        #     SETTINGS.write(configfile)

        # self.close()
        pass
        
    
    def ChangeFile(self):
        self.CHP = Change_profession(self.proffession_number)
        self.CHP.show()
        self.CHP.OK_button.clicked.connect(self.Restart)
    
    def Restart(self):
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
        print(status)
        

    def add_data(self):

        #ДОБАВЯЕМ РАБОЧИЙ КАЛЕНДАРЬ
        #TODO
        x = 0
        work_column=3
        for data in range(1,33):
            if data <16:
                item = QStandardItem(str(data))
                #делаем его нередактируемым
                item.setEditable(False)
                self.model.setItem(x, work_column, item)
                work_column+=1
            elif data == 16 :
                item = QStandardItem("-")
                item.setEditable(False)
                self.model.setItem(x, work_column, item)
                work_column+=1
            else:
                item = QStandardItem(str(data-1))
                item.setEditable(False)
                self.model.setItem(x+1, work_column-16, item)
                work_column+=1

        # добавляем коряво ячейки TODO
        x=1+1
        work_column =0
        #задаем начальный столбец
        for tabel in self.tabels:
            #создаем итем
            item = QStandardItem("")
            #делаем его нередактируемым
            self.model.setItem(x, work_column, item)
            x=x+2
        # ДОБАВЛЯЕМ ТАБЕЛЬНЫЕ

        x=1+1
        work_column =0
        #задаем начальный столбец
        for tabel in self.tabels:
            #создаем итем
            item = QStandardItem(tabel)
            #делаем его нередактируемым
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            self.data_table_view.setSpan(x,work_column,2,1)
            x=x+2

        work_column+=1
        
        
        # ДОБАВЛЯЕМ ФАМИЛИИ
        x = 1+1
        for tabel in self.tabels:
            item = QStandardItem(self.tabels[tabel]["фамилия"])
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            x=x+2

        # ДОБАВЛЯЕМ ИНИЦИАЛЫ
        x = 2+1
        for tabel in self.tabels:
            item = QStandardItem(self.tabels[tabel]["инициалы"])
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            x=x+2
        
        work_column+=1

        # ДОБАВЛЯЕМ РАЗРЯДЫ

        x = 1+1
        for tabel in self.tabels:
            item = QStandardItem(str(self.tabels[tabel]["разряд"]))
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            self.data_table_view.setSpan(x,work_column,2,1)
            x=x+2
        
        work_column+=1


        # ДОБАВЛЯЕМ ГРАФИК ОТРАБОТАННЫХ СМЕН
        x = 1+1
        for tabel in self.tabels:
            for day in range(0,len(self.tabels[tabel]["отработанные смены"])):
                if day<16:
                    item = QStandardItem(str(self.tabels[tabel]["отработанные смены"][day]))
                    item.setEditable(False)
                    self.model.setItem(x, day+work_column,item )
                else:
                    item = QStandardItem(str(self.tabels[tabel]["отработанные смены"][day]))
                    item.setEditable(False)
                    self.model.setItem(x+1, day+work_column-16, item)
            x=x+2
        
        work_column+=16

        # ДОБАВЛЯЕМ ЯЧЕЙКИ В КОТОРЫЕ БУДЕМ ЗАНОСИТЬ ТАБЕЛЬНЫЕ ЗАМЕЩАЮЩИХ(рабочая часть с правой стороны)
        
        x = 1+1
        work_row = x
        for x in range(work_row,len(self.tabels)*2+work_row):
            for y in range(0,16):
                item = QStandardItem(None)
                # делаем их все нередактируемые и заполняем цветом
                item.setEditable(False)
                item.setBackground(QColor(192,192,192))
                self.model.setItem(x, y+work_column, item)
        

    def add_replace_cell(self):
        # РАСКРАШИВАЕМ ЯЧЕЙКИ ТАБЛИЦЫ ГДЕ МОЖНО ДАТЬ ЗАМЕЩЕНИЕ

        # НАЧАЛЬНАЯ КОЛОНКа # TODO сделать чтобы она изменялась по всему документу
        work_column = 18+1
        # НАЧАЛЬНАЯ СТРОКА # TODO сделать чтобы она изменялась по всему документу
        x = 1+1
        # пробегаемся по табельным
        for tabel in self.tabels:
            # Итерируем рабочий календарь по количеству дней
            for day in range(1,len(self.all_data["шифр"][self.proffession_number]["Рабочий календарь"])):
                # Проверяем есть ли в день у указанного табельного замещающие(если есть, значит отмечаем в таблице этот день)
                if self.tabels[tabel]["Замещающие"].get(str(day)) !=None:
                    # если дни <16 это первая строка
                    if day<16:
                        item = QStandardItem("")
                        item.setBackground(QColor(0,128,128))
                        self.model.setItem(x, day+work_column-1,item)
                    # если дни=>16 вторая строка
                    else:
                        item = QStandardItem("")
                        item.setBackground(QColor(0,128,128))
                        self.model.setItem(x+1, day+work_column-16,item)
            x=x+2


    def input_user_color_and_save(self):
        # загружаем данные из файла, и если файла нет используем пустой словарь
        try:
            # извлекаем из JSON год и месяц
            self.year=self.all_data["шифр"][self.proffession_number]["год_месяц"][0]
            self.month = self.all_data["шифр"][self.proffession_number]["год_месяц"][1]
            self.TEMP = QSettings(f'{self.year}\\{self.month}\\data\\{self.proffession_number}_input.ini', QSettings.IniFormat)
            
            data_dict_from_input_user = self.TEMP.value('input_user')
            data_dict_from_input_user = eval(data_dict_from_input_user)
            save_input_user_for_load_in_file = data_dict_from_input_user
            
            data_dict_from_summ = self.TEMP.value("for_summ")
            data_dict_from_summ = eval(data_dict_from_summ)
            save_input_user_for_summ_in_file = data_dict_from_summ
        except:
            save_input_user_for_load_in_file = {}
            save_input_user_for_summ_in_file = {}
        
        # ПРИНИМАЕМ ОТ ПОЛЬЗОВАТЕЛЯ ВВОД И ОРАШИВАЕМ ЯЧЕЙКИ В ЗАВИСИМОСТИ ОТ ЗНАЧЕНИЯ
        row = self.data_table_view.currentIndex().row()
        column = self.data_table_view.currentIndex().column()

        # Проверяем табельный к которой относится выбранная ячейка.
        # если значение None то поднимаемся на одну строку выше(ячейки обьединенные,значение только в первом)
        if self.model.index(row,0).data() == None:

            try:
                tabel = self.model.index(row-1,0).data()
                date = self.model.index(1,column-16).data()
                user_input = self.data_table_view.currentIndex().data()
                if user_input in self.tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QColor(0,128,0))

                    save_input_user_for_load_in_file[row,column] = user_input, (0,128,0)

                    save_input_user_for_summ_in_file[self.model.index(row-1,0).data(),
                                                    self.model.index(1,column-16).data(),
                                                    ] =  user_input

                elif user_input =="":
                    self.model.item(row, column).setBackground(QColor(0,128,128))
                    try:

                        del save_input_user_for_load_in_file[row,column] 
                        del save_input_user_for_summ_in_file[self.model.index(row-1,0).data(),
                                                    self.model.index(1,column-16).data(),
                                                    ]
                    except:
                        pass

                    

                elif user_input not in self.tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QColor(255,0,0))
                    save_input_user_for_load_in_file[row,column] = user_input, (255,0,0)

                    save_input_user_for_summ_in_file[self.model.index(row-1,0).data(),
                                                    self.model.index(1,column-16).data()
                                                    ] =  user_input

            except KeyError:
                print("-")
        else:
            try:
                tabel = self.model.index(row,0).data()
                date = self.model.index(0,column-16).data()
                user_input = self.data_table_view.currentIndex().data()
                if user_input in self.tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QColor(0,128,0))
                    save_input_user_for_load_in_file[row,column] = user_input, (0,128,0)
                    save_input_user_for_summ_in_file[self.model.index(row,0).data(),
                                                    self.model.index(0,column-16).data()
                                                    ] = user_input

                elif user_input =="":
                    self.model.item(row, column).setBackground(QColor(0,128,128))
                    try:

                        del save_input_user_for_load_in_file[row,column] 
                        del save_input_user_for_summ_in_file[self.model.index(row,0).data(),
                                                        self.model.index(0,column-16).data()
                                                        ]
                    except:
                        pass

                elif user_input not in self.tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QColor(255,0,0))
                    save_input_user_for_load_in_file[row,column] = user_input, (255,0,0)
                    save_input_user_for_summ_in_file[self.model.index(row,0).data(),
                                                    self.model.index(0,column-16).data()
                                                    ] = user_input
            except KeyError:
                print("-")
        
        self.TEMP.setValue("input_user", str(save_input_user_for_load_in_file))
        # self.settings.beginGroup("406")
        self.TEMP.setValue("for_summ", str(save_input_user_for_summ_in_file))
        # self.settings.endGroup()
        print(save_input_user_for_load_in_file)
        print(save_input_user_for_summ_in_file)


    def load_data(self):
        try:
            self.year=self.all_data["шифр"][self.proffession_number]["год_месяц"][0]
            self.month = self.all_data["шифр"][self.proffession_number]["год_месяц"][1]
            
            self.TEMP = QSettings(f'{self.year}\\{self.month}\\data\\{self.proffession_number}_input.ini', QSettings.IniFormat)
            data_dict = self.TEMP.value('input_user')
        
            data_dict = eval(data_dict)
            
            
            # формат словаря
            # {(строка,ячейка):(табельный,(R,G,B цвет))
            for Key, Value in data_dict.items():
                row = Key[0]
                column = Key[1]
                item = QStandardItem(Value[0])
                item.setBackground(QColor(Value[1][0],Value[1][1],Value[1][2]))
                self.model.setItem(row, column,item)
        except:
            print("НЕТ ФАЙЛА")
        

    def summ_pay(self):
        # загружаем данные из файла с настройками
        SETTINGS = configparser.ConfigParser()
        SETTINGS.read("data\SETTINGS.ini", encoding="utf-8")
        SETTINGS_TEMP_PATH = SETTINGS["Settings"][f"path_with_input_{self.proffession_number}"]

        INPUT_TEMP = configparser.ConfigParser()
        INPUT_TEMP.read(SETTINGS_TEMP_PATH, encoding="utf-8")
        payment_list = []
        list_tabel = []
        day = 21
        cofficient = 0.24
        try:
            data_dict = INPUT_TEMP["General"]["for_summ"]
            data_dict = json.loads(data_dict)
            data_dict = eval(data_dict)
            def summ_tabel(prof):
                if prof == 3:
                    money = (int(SETTINGS[self.proffession_number]["cv_three_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day) + (int(SETTINGS[self.proffession_number]["cv_three_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day*cofficient)  
                elif prof == 4:
                    money = (int(SETTINGS[self.proffession_number]["cv_four_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day) + (int(SETTINGS[self.proffession_number]["cv_four_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day*cofficient)
                elif prof == 5:
                    money = (int(SETTINGS[self.proffession_number]["cv_five_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day) + (int(SETTINGS[self.proffession_number]["cv_five_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day*cofficient)
                elif prof == 6:
                    money = (int(SETTINGS[self.proffession_number]["cv_six_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day) + (int(SETTINGS[self.proffession_number]["cv_six_tarif"])*int(SETTINGS[self.proffession_number]["procent_text"])*0.01/day*cofficient)
                return float('{:.2f}'.format(money))
            new_dict = {}
            # Пробегаемся по всем табельным
            for tabel in  self.tabels:
                # создаем для каждого табельного свой список замещающик
                list_tabel = []
                # создаем для каждого табельного словарь(замещающий: сумма)
                new_dict ={}
                # пробегаемся по значениям (ТАБЕЛЬНЫЙ, дата): табельный замещающего
                for Key, Value in data_dict.items():
                    # Проверяем если табельные совпадают
                    if Key[0] == tabel:
                        # задаем разряд
                        prof = self.tabels[tabel]["разряд"]
                        # задаем сумму для данного разряда
                        money = summ_tabel(prof)
                        # Добавляем в список табельный
                        list_tabel.append(Value)
                        # Создаем словарь (Табельный, сколько раз повторяется)
                        c = Counter(list_tabel)
                        new_dict ={}
                        for key,value in dict(c).items():
                            new_dict[Key[0],key] =int(value)*money
                        # print(new_dict)
                if new_dict == {}:
                    continue
                else:
                    payment_list.append(new_dict)

                    
                        
                            # if new_dict not in payment_list:
                            #     payment_list.append(new_dict)
            print(new_dict)
            print(dict(c))
            print(payment_list)
            
        except:
            print(f'[INFO] -в блоке SUMM_PAY- {Exception}')

                  
    def parameters(self):
        #Задаем параметры таблицы
        self.data_table_view.setModel(self.model)
        # self.data_table_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.data_table_view.horizontalHeader().setMinimumSectionSize(30)
        self.data_table_view.resizeColumnsToContents()
        #Показывае данные при изменении в ячейке
        self.model.itemChanged.connect(self.input_user_color_and_save)
        self.model.itemChanged.connect(self.summ_pay)
        self.top_layout.addWidget(self.data_table_view)
    
    
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MAIN_WORK_TABLE("87100")
    main.show()
    sys.exit(app.exec_())
