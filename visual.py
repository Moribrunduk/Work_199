import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json


with open("data\\all_data2.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle("Расчет 199 премии")
        self.top_layout = QVBoxLayout()
        self.setLayout(self.top_layout)
        self.resize(500, 300)

        self.data_table_view = QTableView()
        self.model = QStandardItemModel(self)
        # self.model.setHorizontalHeaderItem(0, QStandardItem("Имя"))
        # self.model.setHorizontalHeaderItem(1, QStandardItem("Пол"))
        # self.model.setHorizontalHeaderItem(2, QStandardItem("Вес (кг)"))

        # for row in range(3):                                   # 2
        #     for column in range(3):
        #         item = QStandardItem('({}, {})'.format(row, column))
        #         self.model.setItem(row, column, item)

        # #self.model.setItem()
        # item1 = QStandardItem("Лелей")
        # self.model.setItem(0, 0, item1)

        # item2 = QStandardItem('мужчина')
        # self.model.setItem(0, 1, item2)

        # item3 = QStandardItem('70')
        # self.model.setItem(0, 2, item3)

        self.model.appendRow([QStandardItem('Hanme'), QStandardItem('Женский'), QStandardItem('60'), QStandardItem('Пожалуйста'),QStandardItem('Пожалуйста')])
        # self.model.insertRow(4, [QStandardItem('Джим'), QStandardItem('мужчина'), QStandardItem('65')])
        self.data_table_view.setModel(self.model)

        # self.data_table_view.horizontalHeader().setStretchLastSection(True)
        self.data_table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.data_table_view.clicked.connect(self.show_info)

        # self.info_label = QLabel(self)
        # self.info_label.setAlignment(Qt.AlignCenter)

        self.top_layout.addWidget(self.data_table_view)
        # self.top_layout.addWidget(self.info_label)

    # def show_info(self):
    #     row = self.data_table_view.currentIndex().row()
    #     column = self.data_table_view.currentIndex().column()
    #     print('({}, {})'.format(row, column))

    #     data = self.data_table_view.currentIndex().data()
    #     self.info_label.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()

    sys.exit(app.exec_())


