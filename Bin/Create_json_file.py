import os
import xlrd
import json
import configparser



class CREATE_JSON_DATA():
    def __init__(self,profession_number):
        # super(CREATE_JSON_DATA,self).__init__()
        self.profession_number = profession_number
    def main(self):
        self.create_file()
        self.get_data_personal_87100()
 
    def create_file_SETTINGS(self):
        
        settings = configparser.ConfigParser()
        settings["Settings"] = {}
        settings["Settings"]["Path_87100"] = ""
        settings["Settings"]["Path_87200"] = ""
        settings["Settings"]["Path_08300"] = ""
        settings["87100"] = {"cv_three_tarif":1,
                                "cv_four_tarif":0,
                                "cv_five_tarif":0,
                                "cv_six_tarif":0,
                                "procent_text":0}
        settings["87200"] = {"cv_three_tarif":0,
                                "cv_four_tarif":0,
                                "cv_five_tarif":0,
                                "cv_six_tarif":0,
                                "procent_text":0}
        settings["08300"] = {"cv_three_tarif":0,
                                "cv_four_tarif":0,
                                "cv_five_tarif":0,
                                "cv_six_tarif":0,
                                "procent_text":0}
        settings["Days"] = {}                        
        settings["Days"]["days_keys"]=str(['"ИО" - ', '"О" - ', '"Э" - ', '"Р" - ', '"А" - ', '"Ж" - ', '"Д" - ', '"М" - ', '"Б" - ', '"К" - '])
        settings["Days"]["days_values"]=str(['И.о.мастера', 'Отпуск очередной', 'Отпуск учебный', 'Отпуск по беремености', 'Отпуск за свой счет', 'Пенсионный день/уход за детьми', 'Донорский день', 'Медкомиссия', 'Больничный', 'Командировка'])
    
        with open("data\SETTINGS.ini", "w", encoding="utf-8") as configfile:
            settings.write(configfile)

    def create_file(self):
        if os.path.isfile("data/SETTINGS.ini") == False:
            self.create_file_SETTINGS()

    def get_data_personal_87100(self):

        # загружаем рабочий файл 
        settings = configparser.ConfigParser()
        settings.read("data/SETTINGS.ini", encoding="utf-8")
        work_book = xlrd.open_workbook(settings["Settings"][f'Path_{self.profession_number}'])
        # загружаем рабочий лист
        work_sheet = work_book.sheet_by_name("Табель")

        all_data = {}

        # создаем словарь в ключе "шифр" с профессиями
        all_data["шифр"]= [self.profession_number]
        # превращаем список в словарь с ключами
        all_data["шифр"] = dict.fromkeys(all_data["шифр"])

        all_data["шифр"][self.profession_number] = {"Табельный":[]}
        all_data["шифр"][self.profession_number]["Табельный"]={}

        # ищем ячейку с которой начинается шифр профессии
        for row in range(0,work_sheet.nrows):
            x = work_sheet.cell(row,4).value
            if x == self.profession_number:
                start_row = row-2
                break
        
        # ищем последнюю ячейку для данного шифра профессии
        for row in range(start_row,work_sheet.nrows):
            x = work_sheet.cell(row,4).value
            if x != self.profession_number:
                final_row = row
                break

        
        # создаем календарь рабочего времени(для програмного расчета, начало с 0 последнее число 32)
        base_calendar = []
        for row in range(9,10+1):
            for cell in range(6,22):
                if work_sheet.cell(row,cell).value == "-":
                    base_calendar.append(work_sheet.cell(row,cell).value)
                else:
                    base_calendar.append(int(work_sheet.cell(row,cell).value))
        
        work_time_calendar = {}
        for row in range(9,10+1):
            for i,cell in enumerate(range(6,22)):
                if row ==9:
                    if work_sheet.cell(row,cell).value == "-":
                        work_time_calendar[i+1]=work_sheet.cell(row,cell).value
                    else:
                        work_time_calendar[i+1]=int(work_sheet.cell(row,cell).value)
                if row == 10:
                    if work_sheet.cell(row,cell).value == "-":
                        work_time_calendar[i+1+15]=work_sheet.cell(row,cell).value
                    else:
                        work_time_calendar[i+1+15]=int(work_sheet.cell(row,cell).value)
        
        
        all_data["шифр"][self.profession_number]["Рабочий календарь"]=work_time_calendar

        # заполняем нашу базу данных из файла, по каждому табельному
        all_data["шифр"][self.profession_number]["Табельный"]={}

        #ГЛАВНЫЙ СКРИПТ

        for row in (range(start_row,final_row,2)):
        
            sername = work_sheet.cell(row,2).value
            name = work_sheet.cell(row+1,2).value.replace(" ","")
            qvalification = int(work_sheet.cell(row,3).value)
            tabel_number = int(work_sheet.cell(row,1).value)


            #создаем список выработанных дней по табелю(обновляем с каждой итерацией)
            calendar_time = []
            
            # первая строка в календаре
            for cell in range(6,22):
                
                try:
                    #первый символ переводим в число
                    calendar_time.append(int(work_sheet.cell(row,cell).value[0]))
                except:
                    # тип float вылетает тоже в ексепт, поэтому переводим его в число
                    if type(work_sheet.cell(row,cell).value) == float:
                        calendar_time.append(int(work_sheet.cell(row,cell).value))
                    else:
                    # остальное все оставляем как есть
                        calendar_time.append(work_sheet.cell(row,cell).value)
                
            # вторая строка в календаре
            for cell in range(6,22):
                try:
                    #первый символ переводим в число
                    calendar_time.append(int(work_sheet.cell(row+1,cell).value[0]))
                except:
                    # тип float вылетает тоже в ексепт, поэтому переводим его в число
                    if type(work_sheet.cell(row+1,cell).value) == float:
                        calendar_time.append(int(work_sheet.cell(row+1,cell).value))
                    else:
                    # остальное все оставляем как есть
                        calendar_time.append(work_sheet.cell(row+1,cell).value)
            
            # создаем список пропущенных дней+ словарь в котором указаны пропущенные дни и причина пропуска
        
            missed_day = []
            missed_day_dict ={}

            for x in range(0,len(base_calendar)):
                # проверяем условие, если отработанный день не совпадает с графиком смен(выходные залетают в несовпадение)
                if calendar_time[x] != base_calendar[x] :
                #проверяем условие, что если по графику смен "-" а в табеле(7 или 8) отработан выходной
                # (чтобы не попасть в пропущенную смену)
                        # из за особенностей калкендаря, т,к отчет начинается с 0, а даты с 1го числа
                        # но в календаре после 15 числа стоит "-" а дальше переходит на следующую строку
                    if x<15:
                        if calendar_time[x] == 7:
                            continue
                        missed_day.append(x+1)
                        missed_day_dict[x+1] = calendar_time[x]
                
                    else:
                        if calendar_time[x] == 7:
                            continue
                        missed_day.append(x)
                        missed_day_dict[x] = calendar_time[x]

            all_data["шифр"][self.profession_number]["Табельный"][tabel_number] = {
                    "фамилия":sername,
                    "инициалы":name,
                    "разряд":qvalification,
                    "отработанные смены":calendar_time,
                    "Пропущенные смены": missed_day,
                    "Причина пропуска смен": missed_day_dict
                }
        #создание папки
        data_year = work_sheet.cell(1,0).value
        print(data_year)
        data_month = work_sheet.cell(1,2).value
        print(data_month)
        if not os.path.isdir("data"):
            os.mkdir("data")
        with open(f"data/{self.profession_number}_{data_month}_{data_year}.json", "w", encoding="utf-8") as file:
                json.dump(all_data,file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    m = CREATE_JSON_DATA(87100)
    m.main()