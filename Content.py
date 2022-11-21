import sys
sys.path.insert(1,"Bin\Settings_form_window")
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from PyQt5 import QtGui
from collections import Counter

from Bin.Main_table import MainWidget
from Bin.Settings_form_window.Main_settings_window import Settings_window

        
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()


    def initUI(self):
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget()
        self.MAIN_TAB()
        self.SETTINGS_TAB()
        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)
        self.showMaximized()
        

    def MAIN_TAB(self):
        TABLE = MainWidget()
        self.tabWidget.insertTab(1, TABLE, f"Дефек-сты РГГ")
    def SETTINGS_TAB(self):
        SETTINGS = Settings_window()        
        self.tabWidget.insertTab(2, SETTINGS, f"Настройки")     
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MyWindow()
    sys.exit(app.exec_())