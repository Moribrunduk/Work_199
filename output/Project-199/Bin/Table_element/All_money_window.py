import sys
from PyQt5.QtWidgets import QGridLayout, QLabel,QLineEdit,QWidget, QApplication
from PyQt5.QtCore import Qt
import configparser
import json




class ALL_MONEY_WINDOW(QWidget):
    def __init__(self,proffession_number):
        super(ALL_MONEY_WINDOW,self).__init__()
        self.proffession_number = str(proffession_number)
        self.initUI()
        self.Main()
    
        
    def initUI(self):
        
        self.layout = QGridLayout()
        self.setWindowTitle("Сумма")
        self.label_summ = QLabel("Общаяя сумма")
        self.label_summ.setAlignment(Qt.AlignCenter)
        self.label_days = QLabel("Дни на замещение")
        self.label_days.setAlignment(Qt.AlignCenter)

        self.text_summ = QLabel()
        self.text_summ.setStyleSheet("border: 1px solid black;")
        self.text_summ.setAlignment(Qt.AlignCenter)
        self.text_summ.setFixedHeight(20)

        self.text_days = QLabel()
        self.text_days.setStyleSheet("border: 1px solid black;")
        self.text_days.setAlignment(Qt.AlignCenter)
        self.text_days.setFixedHeight(20)
        
        self.layout.addWidget(self.label_summ,0,0)
        self.layout.addWidget(self.text_summ,1,0)
        self.layout.addWidget(self.label_days,2,0)
        self.layout.addWidget(self.text_days,3,0)
        
        self.setFixedSize(320,130)
        self.setLayout(self.layout)
    
    def Main(self):
        self.LoadData()
        self.AllMoney()
        self.ShowDataInLabel()
        
        
    def LoadData(self):
        self.SETTINGS = configparser.ConfigParser()
        self.SETTINGS.read("data/SETTINGS.ini", encoding="utf-8")
        current_path = self.SETTINGS["Settings"][f"current_directory_{self.proffession_number}"]
        with open(f"{current_path}", "r", encoding="utf-8") as file:
            self.all_data = json.load(file)

    def AllMoney(self):   
        hours = self.all_data["шифр"][self.proffession_number]["Информация"]["рабочих_часов"]

        # применям коэффициенты вредности
        if self.proffession_number == "87100":
            self.harmfulness = 0.24
            self.coefficient = int(self.SETTINGS[self.proffession_number]["procent_text"])/100

        elif self.proffession_number == "87200":
            self.harmfulness = 0.04
            self.coefficient = int(self.SETTINGS[self.proffession_number]["procent_text"])/100

        elif self.proffession_number == "08300":
            self.harmfulness = 0.08
            self.coefficient = int(self.SETTINGS[self.proffession_number]["procent_text"])/100
        
# ФУНКЦИЯ ИЗ Main_table.py
        def Summ(personal_number):
            level = self.all_data["шифр"][self.proffession_number]["Табельный"][personal_number]["разряд"]
            if level == 3:
                # тариф
                tarif = int(self.SETTINGS[self.proffession_number]["cv_three_tarif"])
                money_per_hours = (tarif/hours)*self.coefficient
                money_per_hours_in_harmfullness = money_per_hours+money_per_hours*self.harmfulness
                    
            elif level == 4:
                tarif = int(self.SETTINGS[self.proffession_number]["cv_four_tarif"])
                money_per_hours = (tarif/hours)*self.coefficient
                money_per_hours_in_harmfullness = money_per_hours+money_per_hours*self.harmfulness
            elif level == 5:
                tarif = int(self.SETTINGS[self.proffession_number]["cv_five_tarif"])
                money_per_hours = (tarif/hours)*self.coefficient
                money_per_hours_in_harmfullness = money_per_hours+money_per_hours*self.harmfulness
            elif level == 6:
                tarif = int(self.SETTINGS[self.proffession_number]["cv_six_tarif"])
                money_per_hours = (tarif/hours)*self.coefficient
                money_per_hours_in_harmfullness = money_per_hours+money_per_hours*self.harmfulness
            return float('{:.2f}'.format(money_per_hours_in_harmfullness))

        all_summ = 0
        for tabel in self.all_data["шифр"][self.proffession_number]["Табельный"]:
            sum_hours = 0
            for key in (self.all_data["шифр"][self.proffession_number]["Табельный"][tabel]["Замещающие"]).keys():
                missed_hours = (self.all_data["шифр"][self.proffession_number]["Рабочий календарь"][str(key)])
                sum_hours+=missed_hours
            all_summ += Summ(tabel)*sum_hours
        all_summ = ('{:.2f}'.format(all_summ))
        
        
        all_missed_days = 0
        for tabel in self.all_data["шифр"][self.proffession_number]["Табельный"]:
                missed_days = self.all_data["шифр"][self.proffession_number]["Табельный"][tabel]["Замещающие"].keys()
                all_missed_days+=len(missed_days)

        return (all_summ,str(all_missed_days))
                
    def ShowDataInLabel(self):
        summ = self.AllMoney()[0]
        days = self.AllMoney()[1]
        self.text_summ.setText(summ)
        self.text_days.setText(days)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    AMW = ALL_MONEY_WINDOW("87100")
    AMW.show()
    sys.exit(app.exec_())