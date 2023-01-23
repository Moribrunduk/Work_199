import os
import xlrd
import json
import configparser



class CREATE_JSON_DATA():
    def __init__(self,profession_number):
        self.profession_number = str(profession_number)
    def main(self):
        self.get_data_personal()
        self.day_for_personal()

    def get_data_personal(self):

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
                start_row = row
                # start_row = row-2
                print(start_row)
                break
        
        # ищем последнюю ячейку для данного шифра профессии
        for row in range(start_row,work_sheet.nrows,2):
            x = str(work_sheet.cell(row,4).value)
            x = x.partition(".")[0]
            
            if str(x) == str(self.profession_number):
                # +2 чтобы цеплял последнего человека([TEST])
                final_row = row+2
                
           
           
        # создаем календарь рабочего времени(для програмного расчета, начало с 0 последнее число 32)
        base_calendar = []
        for row in range(9,10+1):
            for cell in range(6,22):
                if work_sheet.cell(row,cell).value == "-":
                    base_calendar.append(work_sheet.cell(row,cell).value)
                else:
                    base_calendar.append(int(work_sheet.cell(row,cell).value))
        
        work_time_calendar = {}
        print(self.profession_number)
        if self.profession_number == "87100":
           
            start_row_work_calendar = 9
        elif self.profession_number == "87200" or "08300":
            
            start_row_work_calendar = 7
        for row in range(start_row_work_calendar,start_row_work_calendar+2):
        # for row in range(9,10+1):
            for i,cell in enumerate(range(6,22)):
                if row == start_row_work_calendar:
                    if work_sheet.cell(row,cell).value == "-":
                        work_time_calendar[i+1]=work_sheet.cell(row,cell).value
                    else:
                        work_time_calendar[i+1]=int(work_sheet.cell(row,cell).value)
                if row == start_row_work_calendar+1:
                    if work_sheet.cell(row,cell).value == "-":
                        work_time_calendar[i+1+15]=work_sheet.cell(row,cell).value
                    else:
                        work_time_calendar[i+1+15]=int(work_sheet.cell(row,cell).value)
        print(work_time_calendar)                        
        
        # добавляем рабочий календарь
        all_data["шифр"][self.profession_number]["Информация"] = {}
        all_data["шифр"][self.profession_number]["Информация"]["год"] = (work_sheet.cell(1,0).value.replace(" ",''))
        all_data["шифр"][self.profession_number]["Информация"]["месяц"] = (work_sheet.cell(1,2).value)
        if self.profession_number == "87100":
            all_data["шифр"][self.profession_number]["Информация"]["рабочих_дней"] = int(work_sheet.cell(9,23).value)
            all_data["шифр"][self.profession_number]["Информация"]["рабочих_часов"] = int(work_sheet.cell(9,22).value)
        elif self.profession_number == "87200" or "87300":
            all_data["шифр"][self.profession_number]["Информация"]["рабочих_дней"] = int(work_sheet.cell(7,23).value)
            all_data["шифр"][self.profession_number]["Информация"]["рабочих_часов"] = int(work_sheet.cell(7,22).value)

        all_data["шифр"][self.profession_number]["Рабочий календарь"] = work_time_calendar

        # # заполняем нашу базу данных из файла, по каждому табельному
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
                    calendar_time.append(int(work_sheet.cell(row,cell).value))
                    # TODO
                    # calendar_time.append(int(work_sheet.cell(row,cell).value[0]))
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
                    # calendar_time.append(int(work_sheet.cell(row+1,cell).value[0]))
                    # TODO
                    calendar_time.append(int(work_sheet.cell(row+1,cell).value))
                except:
                    # тип float вылетает тоже в ексепт, поэтому переводим его в число
                    if type(work_sheet.cell(row+1,cell).value) == float:
                        calendar_time.append(int(work_sheet.cell(row+1,cell).value))
                    else:
                    # остальное все оставляем как есть
                        calendar_time.append(work_sheet.cell(row+1,cell).value)
            
# создаем список пропущенных дней+ словарь в котором указаны пропущенные дни и причина пропуска
# ###############################################################################
            missed_day = []
            missed_day_dict ={}
            name_missed = settings["Days"]["days_keys"]
            
            # проверяем есть ли причина отсутствия которая есть в файле SETTINGS
            for x in range(0,len(base_calendar)):
                print(calendar_time[x])
                if str(calendar_time[x]) in name_missed:
                    if x<15:
                        missed_day.append(x+1)
                        missed_day_dict[x+1] = calendar_time[x]
                    else:
                        missed_day.append(x)
                        missed_day_dict[x] = calendar_time[x]
            # проверяем чтобы совпадали часы(если человек брал за свой счет сколько то часов)
                elif str(calendar_time[x])[0] != str(base_calendar[x]):
                    if x<15:
                        if str(calendar_time[x])[0] == "7":
                            continue
                        missed_day.append(x+1)
                        missed_day_dict[x+1] = calendar_time[x]
                    else:
                        if str(calendar_time[x])[0] == "7":
                            continue
                        missed_day.append(x)
                        missed_day_dict[x] = calendar_time[x]
            # Проверяем на замещение
                elif str(calendar_time[x])[1:3] in ("МН","мн","МВ","мв","МД","мд","м","М"):
                    if x<15:
                        missed_day.append(x+1)
                        missed_day_dict[x+1] = calendar_time[x]
                    else:
                        missed_day.append(x)
                        missed_day_dict[x] = calendar_time[x]


                

##############################################################################
            all_data["шифр"][self.profession_number]["Табельный"][tabel_number] = {
                    "фамилия":sername,
                    "инициалы":name,
                    "разряд":qvalification,
                    "отработанные смены":calendar_time,
                    "Пропущенные смены": missed_day,
                    "Причина пропуска смен": missed_day_dict
                }
        self.data_year = work_sheet.cell(1,0).value.replace(" ","")
        
        self.data_month = work_sheet.cell(1,2).value
       
        self.file_path = (f"{self.data_year}\\{self.data_month}\\data")
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
        with open(f"{self.file_path}/{self.profession_number}_{self.data_month}_{self.data_year}.json", "w", encoding="utf-8") as file:
                json.dump(all_data,file, ensure_ascii=False, indent=4)
        
    def day_for_personal(self):
        
        with open(f"{self.file_path}/{self.profession_number}_{self.data_month}_{self.data_year}.json", "r", encoding="utf-8") as file:
            all_data = json.load(file)

        # Обьединяем со вторым файлом 
        for personal_number in all_data["шифр"][self.profession_number]["Табельный"]:

        # каждому табельному создаем словарь
            personal_number_for_him_dict = {}

            # пробегаемся у этого табельного по пропущенным сменам
            for data in all_data["шифр"][self.profession_number]["Табельный"][personal_number]["Пропущенные смены"]:
                #Проверяем если в причине пропущеной смены цифра(значит, человек брал часы), пропускаем этот день
                try:
                    if str(all_data["шифр"][self.profession_number]["Табельный"][personal_number]["Причина пропуска смен"][str(data)])[0] in ("0","1","2","3","4","5","6","7","8"):

                        if str(all_data["шифр"][self.profession_number]["Табельный"][personal_number]["Причина пропуска смен"][str(data)])[1:3] not in ("МН","мн","МВ","мв","МД","мд","м","М"):
                            continue

                    # проверяем совпадает ли день на замещение с выходным, пропускаем этот день


                    elif all_data["шифр"][self.profession_number]["Рабочий календарь"][str(data)]=="-":
                        continue
                except: IndexError
                
                

                # создаем список людей которые могут замещать в пропущенную смену
                personal_number_for_him_in_data = []

                #пробегаем по всем табельным и проверяем кто не отсутствовал в указанную дату
                for item in all_data["шифр"][self.profession_number]["Табельный"]:
                    # исключаем из списка табельный проверяемого
                    if item == personal_number:
                        continue
                    # print(f'{item}---{all_data["шифр"][self.profession_number]["Табельный"][item]["Пропущенные смены"]}')
                    if data not in all_data["шифр"][self.profession_number]["Табельный"][item]["Пропущенные смены"]:
                        #добавлеям в список табельные которые могут замещать на конкретную дату
                        personal_number_for_him_in_data.append(item)
                    
                    #заполняем словарь по датам
                    personal_number_for_him_dict[data]=personal_number_for_him_in_data
            # добавляем словарь каждому табельному
            all_data["шифр"][self.profession_number]["Табельный"][personal_number]["Замещающие"]=personal_number_for_him_dict

        #создание папки
        with open(f"{self.file_path}/{self.profession_number}_{self.data_month}_{self.data_year}.json", "w", encoding="utf-8") as file:
                json.dump(all_data,file, ensure_ascii=False, indent=4)
        
        settings = configparser.ConfigParser()
        settings.read("data/SETTINGS.ini", encoding="utf-8")
        settings["Settings"][f"current_directory_{self.profession_number}"] = f"{self.file_path}\{self.profession_number}_{self.data_month}_{self.data_year}.json"
        with open("data\SETTINGS.ini", "w", encoding="utf-8") as configfile:
            settings.write(configfile)

if __name__ == "__main__":
    m = CREATE_JSON_DATA("87200")
    m.main()