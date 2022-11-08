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





class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        
        self.tabWidget = QtWidgets.QTabWidget()
        count = self.tabWidget.count()
        self.nb = QtWidgets.QToolButton(text="Добавить", autoRaise=True)
        self.nb.clicked.connect(self.new_tab)
        self.tabWidget.insertTab(count, QtWidgets.QWidget(), "")
        self.tabWidget.tabBar().setTabButton(
            count, QtWidgets.QTabBar.RightSide, self.nb)

        self.new_tab()

        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)

        # self.statusBar().showMessage('Message in statusbar. '
            # 'Будет Скрыто через 5000 миллисекунд - 5 секунды! ', 5000)

    def new_tab(self):
        index = self.tabWidget.count() - 1
        tabPage = MyTab(self)        
        self.tabWidget.insertTab(index, tabPage, f"Tab {index}")
        self.tabWidget.setCurrentIndex(index)
        tabPage.lineEdit.setFocus()        
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
    win = MyWindow()
    win.resize(640, 480)
    win.show()
    sys.exit(app.exec_())