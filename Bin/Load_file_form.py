import sys
sys.path.insert(1,"Bin")
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QHBoxLayout,QFileDialog,QVBoxLayout,QLabel,QFrame
from PyQt5.QtCore import Qt
import configparser
import xlrd

from Create_json_file import CREATE_JSON_DATA

class Change_profession(QWidget):
    def __init__(self,profession_number):
        super(Change_profession,self).__init__()
        self.profession_number = str(profession_number)
        self.initUI()
        
    def initUI(self):

        self.setWindowTitle("Выбор Файла")
        self.setFixedSize(450,150)
        self.main_layout = QHBoxLayout()
        self.main_button = QPushButton(f"Добавьте табель для \n дефектоскопистов РГГ \n ({self.profession_number})")
        self.main_button.clicked.connect(self.get_file_directory)
        self.main_button.setStyleSheet("font: 14pt")
        self.main_button.setFixedSize(250,130)
        

        self.right_layout = QVBoxLayout()
        self.file_label = QLabel("Выберите файл")
        self.file_label.setStyleSheet("font: 10pt")
        self.file_label.setAlignment(Qt.AlignCenter)

        self.right_layout_for_button = QHBoxLayout()
        self.OK_button = QPushButton("OK")
        self.change_button = QPushButton("Изменить")
        self.change_button.clicked.connect(self.get_file_directory)
        self.right_layout_for_button.addWidget(self.OK_button)
        self.right_layout_for_button.addWidget(self.change_button)

        self.right_layout.addWidget(self.file_label)
        self.right_layout.addLayout(self.right_layout_for_button)

        self.main_layout.addWidget(self.main_button)
        self.main_layout.addLayout(self.right_layout)

        self.setLayout(self.main_layout)

    def get_file_directory(self):
        settings = configparser.ConfigParser()
        settings.read("data\SETTINGS.ini",encoding="utf-8")
        filepath, filetype = QFileDialog.getOpenFileName(self,
                             "Выбрать файл",
                             ".",
                             "Text Files(*.xls)")
        settings["Settings"][f'Path_{self.profession_number}'] = filepath

        work_book = xlrd.open_workbook(filepath)
        work_sheet = work_book.sheet_by_name("Табель")
        data_year = work_sheet.cell(1,0).value
        print(data_year)
        data_month = work_sheet.cell(1,2).value
        print(data_month)
        with open("data\SETTINGS.ini", "w", encoding="utf-8") as configfile:
            settings.write(configfile)
        self.file_label.setText(f"{data_month} {data_year}")

        self.CREATE_JSON_FILE = CREATE_JSON_DATA(int(self.profession_number))
        self.CREATE_JSON_FILE.main()

        
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    CP = Change_profession(87100)
    CP.showMaximized()
    sys.exit(app.exec_())