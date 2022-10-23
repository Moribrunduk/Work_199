from sqlite3 import Row
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import json


with open("data\\all_data2.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

# разрработано для работы по одному шифру

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
        
        item1 = QStandardItem("Лелей")
        # ДОБАВЛЯЕМ ТАБЕЛЬНЫЕ

        #задаем начальный столбец
        x = 0
        work_column = 0
        for tabel in tabels:
            item = QStandardItem(tabel)
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            self.data_table_view.setSpan(x,0,2,1)
            x=x+2

        work_column+=1
        
        
        # ДОБАВЛЯЕМ ФАМИЛИИ
        x = 0
        for tabel in tabels:
            item = QStandardItem(tabels[tabel]["фамилия"])
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            x=x+2
        # ДОБАВЛЯЕМ ИНИЦИАЛЫ
        x = 1
        for tabel in tabels:
            item = QStandardItem(tabels[tabel]["инициалы"])
            item.setEditable(False)
            self.model.setItem(x, work_column, item)
            x=x+2
        
        work_column+=1

        # ДОБАВЛЯЕМ ГРАФИК ОТРАБОТАННЫХ СМЕН
        x = 0
        for tabel in tabels:
            for day in range(0,len(tabels[tabel]["отработанные смены"])):
                if day<16:
                    item = QStandardItem(QStandardItem(str(tabels[tabel]["отработанные смены"][day])))
                    item.setEditable(False)
                    self.model.setItem(x, day+work_column,item )
                else:
                    item = QStandardItem(QStandardItem(str(tabels[tabel]["отработанные смены"][day])))
                    item.setEditable(False)
                    self.model.setItem(x+1, day+work_column-16, item)
            x=x+2
        
        work_column+=16

        # ДОБАВЛЯЕМ ЯЧЕЙКИ В КОТОРЫЕ БУДЕМ ЗАНОСИТЬ ТАБЕЛЬНЫЕ ЗАМЕЩАЮЩИХ
        
        x = 0
        for x in range(0,len(tabels[tabel]["отработанные смены"])*2):
            for y in range(0,16):
                self.model.setItem(x, y+work_column, QStandardItem(""))


        #Задаем параметры таблицы
        self.data_table_view.setModel(self.model)
        # self.data_table_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.data_table_view.horizontalHeader().setMinimumSectionSize(30)
        self.data_table_view.resizeColumnsToContents()
        
        
        
        


        self.top_layout.addWidget(self.data_table_view)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()

    sys.exit(app.exec_())
