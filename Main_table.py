


from operator import truediv
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
                item.setEditable(False)
                self.model.setItem(x, work_column, item)
                work_column+=1
            else:
                item = QStandardItem(str(data-1))
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

        # ДОБАВЛЯЕМ ЯЧЕЙКИ В КОТОРЫЕ БУДЕМ ЗАНОСИТЬ ТАБЕЛЬНЫЕ ЗАМЕЩАЮЩИХ(рабочая часть с правой стороны)
        
        x = 1+1
        work_row = x
        for x in range(work_row,len(tabels)*2+work_row):
            for y in range(0,16):
                item = QStandardItem("")
                # делаем их все нередактируемые и заполняем цветом
                item.setEditable(False)
                item.setBackground(QtGui.QColor(192,192,192))
                self.model.setItem(x, y+work_column, item)
        

    def add_replace_cell(self):
        # РАСКРАШИВАЕМ ЯЧЕЙКИ ТАБЛИЦЫ ГДЕ МОЖНО ДАТЬ ЗАМЕЩЕНИЕ

        # НАЧАЛЬНАЯ КОЛОНКа # TODO сделать чтобы она изменялась по всему документу
        work_column = 18
        # НАЧАЛЬНАЯ СТРОКА # TODO сделать чтобы она изменялась по всему документу
        x = 1+1
        # пробегаемся по табельным
        for tabel in tabels:
            # Итерируем рабочий календарь по количеству дней
            for day in range(1,len(all_data["шифр"]["87100"]["Рабочий календарь"])):
                # Проверяем есть ли в день у указанного табельного замещающие(если есть, значит отмечаем в таблице этот день)
                if tabels[tabel]["Замещающие"].get(str(day)) !=None:
                    # если дни <16 это первая строка
                    if day<16:
                        item = QStandardItem("")
                        item.setBackground(QtGui.QColor(0,128,128))
                        self.model.setItem(x, day+work_column-1,item)
                    # если дни=>16 вторая строка
                    else:
                        item = QStandardItem("")
                        item.setBackground(QtGui.QColor(0,128,128))
                        self.model.setItem(x+1, day+work_column-16,item)
            x=x+2

    def cell_replacement_tabel_list(self):
        pass
    def input_user_and_color(self):
        # ПРИНИМАЕМ ОТ ПОЛЬЗОВАТЕЛЯ ВВОД И ОРАШИВАЕМ ЯЧЕЙКИ В ЗАВИСИМОСТИ ОТ ЗНАЧЕНИЯ
        row = self.data_table_view.currentIndex().row()
        column = self.data_table_view.currentIndex().column()
        # Проверяем табельный к которой относится строка с кликом
        # если значение None то поднимаемся на одну строку выше(ячейки обьединенные,значение только в первом)
        if self.model.index(row,0).data() == None:

            try:
                tabel = self.model.index(row-1,0).data()
                date = self.model.index(1,column-16).data()
                user_input = self.data_table_view.currentIndex().data()
                if user_input in tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QtGui.QColor(0,128,0))

                elif user_input =="":
                    self.model.item(row, column).setBackground(QtGui.QColor(0,128,128))

                elif user_input not in tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QtGui.QColor(255,0,0))

            except KeyError:
                print("-")
        else:
            try:
                tabel = self.model.index(row,0).data()
                date = self.model.index(0,column-16).data()
                user_input = self.data_table_view.currentIndex().data()
                if user_input in tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QtGui.QColor(0,128,0))

                elif user_input =="":
                    self.model.item(row, column).setBackground(QtGui.QColor(0,128,128))

                elif user_input not in tabels[tabel]["Замещающие"][date]:
                    self.model.item(row, column).setBackground(QtGui.QColor(255,0,0))
            except KeyError:
                print("-")
    

    # def show_info(self):
    #     row = self.data_table_view.currentIndex().row()
    #     column = self.data_table_view.currentIndex().column()
    #     print(f'({row}, {column})')
    #     if self.model.index(row,0).data() == None:
    #         print(self.model.index(row-1,0).data())
    #         print(f'ДАТА : {self.model.index(1,column-16).data()}')
    #     else:
    #         print(self.model.index(row,0).data())
    #         print(f'ДАТА : {self.model.index(0,column-16).data()}')

    #     data = self.data_table_view.currentIndex().data()
    #     print(data)
        
                            
    def parameters(self):
        #Задаем параметры таблицы
        self.data_table_view.setModel(self.model)
        # self.data_table_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.data_table_view.horizontalHeader().setMinimumSectionSize(30)
        self.data_table_view.resizeColumnsToContents()
        #Показывае данные при изменении в ячейке
        self.model.itemChanged.connect(self.input_user_and_color)
        #Показывает данные при клике на ячейку
        #[INFO] ---  ИСПОЛЬЗУЕМ ФУНКЦИЮ
        # self.data_table_view.clicked.connect(self.show_info)
        self.top_layout.addWidget(self.data_table_view)
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.add_data()
    main.add_replace_cell()
    main.parameters()
    main.show()

    sys.exit(app.exec_())
