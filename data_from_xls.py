import os
import xlrd
import json
# загружаем рабочий файл 
work_book = xlrd.open_workbook("199шифр.xls")
# загружаем рабочий лист
work_sheet = work_book.sheet_by_name("Табель")

all_data = {}

# создаем словарь в ключе "шифр" с профессиями
all_data["шифр"]= [87100,87200,87300]
# превращаем список в словарь с ключами
all_data["шифр"] = dict.fromkeys(all_data["шифр"])

all_data["шифр"][87100] = {"Табельный":[]}
all_data["шифр"][87100]["Табельный"]={}

# ищем ячейку с которой начинается шифр профессии
for row in range(0,work_sheet.nrows):
    x = work_sheet.cell(row,4).value
    if x == 87100:
        start_row_for_87100 = row
        break

def get_data_personal_87100():
    # создаем календарь рабочего времени
    base_calendar = []
    for row in range(9,10+1):
        for cell in range(6,22):
            if work_sheet.cell(row,cell).value == "-":
                base_calendar.append(work_sheet.cell(row,cell).value)
            else:
                base_calendar.append(int(work_sheet.cell(row,cell).value))

    # заполняем нашу базу данных из файла, по каждому табельному
    all_data["шифр"][87100]["Табельный"]={}

    #ГЛАВНЫЙ СКРИПТ

    for row in (range(start_row_for_87100,work_sheet.nrows,2)):
    
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
                    missed_day.append(x+1)
                    if calendar_time[x] == 7:
                        continue
                    missed_day_dict[x+1] = calendar_time[x]
            
                else:
                    missed_day.append(x)
                    missed_day_dict[x] = calendar_time[x]

        all_data["шифр"][87100]["Табельный"][tabel_number] = {
                "фамилия":sername,
                "инициалы":name,
                "разряд":qvalification,
                "отработанные смены":calendar_time,
                "Пропущенные смены": missed_day,
                "Причина пропуска смен": missed_day_dict
            }
    #создание папки
    if not os.path.isdir("data"):
        os.mkdir("data")
    with open("data\\all_data.json", "w", encoding="utf-8") as file:
            json.dump(all_data,file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    get_data_personal_87100()