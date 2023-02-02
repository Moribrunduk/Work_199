import sys
import os
sys.path.insert(1,"Bin\Settings_form_window")
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QTabWidget,QWidget,QVBoxLayout,QGridLayout
from PyQt5.QtCore import Qt

from Main_table import MAIN_WORK_TABLE
from Settings_form_window.Main_settings_window import Settings_window

from Load_file_form import Change_profession
import configparser

        
class MAIN_WINDOW(QMainWindow):
    def __init__(self):
        super(MAIN_WINDOW,self).__init__()
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.tabWidget = QTabWidget()
        self.Tab_DRGG()
        self.Tab_PZRS()
        self.Tab_FOTO()
        self.SETTINGS_TAB()
        self.layout = QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)
        self.showMaximized()
        

    def Tab_DRGG(self):
        settings = configparser.ConfigParser()
        settings.read("data\SETTINGS.ini",encoding="utf-8")
        if settings["Settings"]["path_87100"] == "":
            TableDRGG = Change_profession("87100")
            TableDRGG.OK_button.clicked.connect(self.load_tab_drgg)
            self.tabWidget.insertTab(1,TableDRGG, f"Дефектоскописты РГГ(87100)")
            
        else:
            if not os.path.isfile(f'{settings["Settings"]["path_87100"]}'):
                TableDRGG = Change_profession("87100")
                TableDRGG.OK_button.clicked.connect(self.load_tab_drgg)
                self.tabWidget.insertTab(1,TableDRGG, f"Дефектоскописты РГГ(87100)")
            else:
                TableDRGG = MAIN_WORK_TABLE("87100")
                self.tabWidget.insertTab(1,TableDRGG, f"Дефектоскописты РГГ(87100)")
        
    
    def load_tab_drgg(self):
        TableDRGG = MAIN_WORK_TABLE("87100")
        self.tabWidget.insertTab(1, TableDRGG, f"Дефектоскописты РГГ(87100)")
        self.tabWidget.removeTab(0)
        
  
    def Tab_PZRS(self):
        settings = configparser.ConfigParser()
        settings.read("data\SETTINGS.ini",encoding="utf-8")
        if settings["Settings"]["path_87200"] == "":
            TablePZRS = Change_profession("87200")
            TablePZRS.OK_button.clicked.connect(self.load_tab_pzrs)
            self.tabWidget.insertTab(2, TablePZRS, f"Дефектоскописты ПЗРС(87200)")

        else:
            if not os.path.isfile(f'{settings["Settings"]["path_87200"]}'):
                TablePZRS = Change_profession("87200")
                TablePZRS.OK_button.clicked.connect(self.load_tab_pzrs)
                self.tabWidget.insertTab(2,TablePZRS, f"Дефектоскописты ПЗРС(87200)")
            else:
                TablePZRS = MAIN_WORK_TABLE("87200")
                self.tabWidget.insertTab(2,TablePZRS, f"Дефектоскописты ПЗРС(87200)")
        
    
    def load_tab_pzrs(self):
        TablePZRS = MAIN_WORK_TABLE("87200")
        self.tabWidget.insertTab(2, TablePZRS, f"Дефектоскописты ПЗРС(87200)")
        self.tabWidget.removeTab(1)

    
    def Tab_FOTO(self):
        settings = configparser.ConfigParser()
        settings.read("data\SETTINGS.ini",encoding="utf-8")

        if settings["Settings"]["path_08300"] == "":
            TableFOTO = Change_profession("08300")
            TableFOTO.OK_button.clicked.connect(self.load_tab_foto)
            self.tabWidget.insertTab(3, TableFOTO, f"Фотолаборанты(08300)")

        else:
            
            if not os.path.isfile(f'{settings["Settings"]["path_08300"]}'):
                TableFOTO = Change_profession("08300")
                TableFOTO.OK_button.clicked.connect(self.load_tab_foto)
                self.tabWidget.insertTab(3,TableFOTO, f"Фотолаборанты(08300)")
            else:
                TableFOTO = MAIN_WORK_TABLE("08300")
                self.tabWidget.insertTab(3,TableFOTO, f"Фотолаборанты(08300)")

            

    def load_tab_foto(self):
        TableFOTO = MAIN_WORK_TABLE("08300")
        self.tabWidget.insertTab(3, TableFOTO, f"Фотолаборанты(08300)")
        self.tabWidget.removeTab(2)
    


    def SETTINGS_TAB(self):
        SETTINGS = Settings_window()        
        self.tabWidget.insertTab(4, SETTINGS, f"Настройки") 
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MAIN_WINDOW()
    sys.exit(app.exec_())