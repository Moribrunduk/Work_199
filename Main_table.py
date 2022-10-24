
import sys
from tracemalloc import start
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from PyQt5 import QtGui


with open("data\\all_data2.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

# разработано для работы по одному шифру

tabels = all_data["шифр"]["87100"]["Табельный"]


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle("Расчет 199 премии")
        self.top_layout = QVBoxLayout()
        self.setLayout(self.top_layout)
        self.resize(500, 300)

        self.data_table_view = QTableView()
        self.model = QStandardItemModel(self)
        
    def add_data(self):

        #ДОБАВЯЕМ РАБОЧИЙ КАЛЕНДАРЬ
        #TODO
        x = 0
        work_column=2
        for data in range(1,33):
            if data <16:
                item = QStandardItem(str(data))
                #делаем его нередактируемым
                item.setEditable(False)
                self.model.setItem(x, work_column, item)
                work_column+=1
            elif data == 16 :
                item = QStandardItem("-")
                #делаем его нередактируемым
                item.setEditable(False)
                self.model.setItem(x, work_column, item)
                work_column+=1
            else:
                item = QStandardItem(str(data-1))
                #делаем его нередактируемым
                item.setEditable(False)
                self.model.setItem(x+1, work_column-16, item)
                work_column+=1



        # ДОБАВЛЯЕМ ТАБЕЛЬНЫЕ

        x=1+1
        work_column =0
        #задаем начальный столбец
        for tabel in tabels:
            #создаем итем
            item = QStandardItem(tabel)
            #делаем его нередактируемым
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            self.data_table_view.setSpan(x,0,2,1)
            x=x+2

        work_column+=1
        
        
        # ДОБАВЛЯЕМ ФАМИЛИИ
        x = 1+1
        for tabel in tabels:
            item = QStandardItem(tabels[tabel]["фамилия"])
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            x=x+2

        # ДОБАВЛЯЕМ ИНИЦИАЛЫ
        x = 2+1
        for tabel in tabels:
            item = QStandardItem(tabels[tabel]["инициалы"])
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            x=x+2
        
        work_column+=1

        # ДОБАВЛЯЕМ ГРАФИК ОТРАБОТАННЫХ СМЕН
        x = 1+1
        for tabel in tabels:
            for day in range(0,len(tabels[tabel]["отработанные смены"])):
                if day<16:
                    item = QStandardItem(str(tabels[tabel]["отработанные смены"][day]))
                    item.setEditable(False)
                    self.model.setItem(x, day+work_column,item )
                else:
                    item = QStandardItem(str(tabels[tabel]["отработанные смены"][day]))
                    item.setEditable(False)
                    self.model.setItem(x+1, day+work_column-16, item)
            x=x+2
        
        work_column+=16

        # ДОБАВЛЯЕМ ЯЧЕЙКИ В КОТОРЫЕ БУДЕМ ЗАНОСИТЬ ТАБЕЛЬНЫЕ ЗАМЕЩАЮЩИХ
        
        x = 1+1
        work_row = x
        for x in range(work_row,len(tabels)*2):
            for y in range(0,16):
                item = QStandardItem("")
                # делаем их все нередактируемые и заполняем цветом
                item.setEditable(False)
                item.setBackground(QtGui.QColor(192,192,192))
                self.model.setItem(x, y+work_column, item)
        

    def add_color_table_he_for_him(self):

        # РАСКРАШИВАЕМ ЯЧЕЙКИ ТАБЛИЦЫ ГДЕ МОЖНО ДАТЬ ЗАМЕЩЕНИЕ

        # НАЧАЛЬНАЯ КОЛОНКа # TODO сделать чтобы она изменялась по всему документу
        work_column = 18
        # НАЧАЛЬНАЯ СТРОКА # TODO сделать чтобы она изменялась по всему документу
        x = 1+1

        # пробегаемся по табельным
        for tabel in tabels:
            
            for day in range(0,len(tabels[tabel]["отработанные смены"])):
                if day<16:
                    if day in tabels[tabel]["Пропущенные смены"]:
                        # ПРОВЕРЯЕМ ЕСЛИ ПРОПУЩЕННЫЕ ДНИ ЭТО ТОЛЬКО ВЗЯТЫЕ ЧАСЫ, ТО НЕ ВКЛЮЧАЕМ ИХ В СПИСОК
                        if tabels[tabel]["Причина пропуска смен"][str(day)] not in range(0,8):
                            item = QStandardItem("")
                            item.setBackground(QtGui.QColor(0,128,128))
                            self.model.setItem(x, day+work_column-1,item)
                else:
                    if day in tabels[tabel]["Пропущенные смены"]:
                        if tabels[tabel]["Причина пропуска смен"][str(day)] not in range(0,8):
                            item = QStandardItem("")
                           
                            item.setBackground(QtGui.QColor(0,128,128))
                            self.model.setItem(x+1, day+work_column-16,item)

            x=x+2

    def show_info(self):
        row = self.data_table_view.currentIndex().row()
        column = self.data_table_view.currentIndex().column()
        print(f'({row}, {column})')
        if self.model.index(row,0).data() == None:
            print(self.model.index(row-1,0).data())
        else:
            print(self.model.index(row,0).data())

        data = self.data_table_view.currentIndex().data()
        print(data)
                            
    def parameters(self):
        #Задаем параметры таблицы
        self.data_table_view.setModel(self.model)
        # self.data_table_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.data_table_view.horizontalHeader().setMinimumSectionSize(30)
        self.data_table_view.resizeColumnsToContents()
        #Показывае данные при изменении в ячейке
        self.model.itemChanged.connect(self.show_info)
        #Показывает данные при клике на ячейку
        self.data_table_view.clicked.connect(self.show_info)
        self.top_layout.addWidget(self.data_table_view)
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.add_data()
    main.add_color_table_he_for_him()
    main.parameters()
    main.show()

    sys.exit(app.exec_())
