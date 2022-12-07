import sys
import os
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Form(QWidget):
    def __init__(self):
        super(Form,self).__init__()
        # self.initUI()
        self.getFileName()


    def initUI(self):
        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setFont(QFont('Arial', 11))

        self.Button = QPushButton("Open File")
        self.Button.clicked.connect(self.getFileName)

        layoutV = QVBoxLayout()
        layoutV.addWidget(self.Button)
      
        layoutH = QHBoxLayout()
        layoutH.addLayout(layoutV)
        layoutH.addWidget(self.plainTextEdit)

        centerWidget = QWidget()
        centerWidget.setLayout(layoutH) 
        self.setCentralWidget(centerWidget)
        
        self.resize(740,480)
        self.setWindowTitle("PyQt5-QFileDialog")


    def getFileName(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                             "Выбрать файл",
                             ".",
                             "Text Files(*.xls)")
        # self.plainTextEdit.appendHtml("<br>Выбрали файл: <b>{}</b> <br> <b>{:*^54}</b>"
        #                               "".format(filename, filetype))
        print(filename)
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())