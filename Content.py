import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from PyQt5 import QtGui
from collections import Counter

from Bin.Main_table import MainWidget



# class MyTab(QtWidgets.QWidget):
#     settings = QSettings("temp.ini", QSettings.IniFormat)
#     def __init__(self, parent=None):
#         super(MyTab, self).__init__()
#         self.parent = parent
#         self.top_layout = QVBoxLayout()
#         self.setLayout(self.top_layout)
#         self.data_table_view = QTableView()
#         self.model = QStandardItemModel(self)
        

class MyTab2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyTab2, self).__init__()
        self.parent = parent
        self.lineEdit = QtWidgets.QLineEdit(placeholderText='таблица2')
        self.tableWidget = QtWidgets.QTableWidget()
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.lineEdit)
        # vbox.addWidget(self.pushButton)
        
    
        

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget()
        self.resize(640, 480)
        # count = self.tabWidget.count()
        self.MAIN_TAB()
        self.new_tab2()
        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)

        # self.statusBar().showMessage('Message in statusbar. '
            # 'Будет Скрыто через 5000 миллисекунд - 5 секунды! ', 5000)

    def MAIN_TAB(self):
        tabPage = MainWidget()
        self.tabWidget.insertTab(1, tabPage, f"Дефек-сты РГГ")
    def new_tab2(self):
        tabPage2 = MyTab2(self)        
        self.tabWidget.insertTab(2, tabPage2, f"Настройки")     
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.showMaximized()
    sys.exit(app.exec_())