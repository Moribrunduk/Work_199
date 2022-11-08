import json
import xlwt
import configparser
import math
import os
from xlutils.copy import copy
from xlrd import open_workbook
from create_form import create_file
from create_form import set_style


# входные данные
profession_code = 87100
month = "03"
year = "22"
tarif = {"87100":{6:9798,5:8910,4:8105,3:7365},"87200":{6:9798,5:8910,4:8105,3:7365},"08300":{6:9798,5:8910,4:8105,3:7365}}
procent = {"87100":"30","87200":"30","08300":"70"}

with open("data\\all_data2.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)
substitutes = configparser.ConfigParser()
substitutes.read('data\datalist of substitutes.ini',encoding='utf-8')


def load_data_and_create_list(profession_code="87100"):

    """
    функция которая загружает данные из файла datalist of subtitutes.ini
    (Замещаемый, причина отсутствия, дата начала отсутствия, замещающий)
    и приводит в список (("Воронов Е.М., табельный 479",
                        "Дефектоскопист РГГ",
                        "Отпуск",
                        "7.11-31.11.2020",
                        "тариф(10988)",
                        "Илюхин Ю.В., табельный 473",
                        "Дефектоскопист РГГ")

    """

    tabels = all_data["шифр"][str(profession_code)]["Табельный"]

    # задаем название професии
    profession_name = ""
    if str(profession_code) == "87100":
        profession_name = "Дефектоскопист РГГ"
    elif str(profession_code) == "87200":
        profession_name = "Дефектоскопист ПЗРС"
    elif str(profession_code) == "08300":
        profession_name = "Фотолаборант"
    else:
        profession_name = "Неизвестный код"

    def print_name(tabel):
        information = all_data["шифр"][str(profession_code)]["Табельный"]
        name = F'{information[tabel]["фамилия"]} {information[tabel]["инициалы"]}'
        return name
    
    def print_reason(reason):

        if reason == "ИО":
            print_reason = "И.о. мастера"
        elif reason == "О":
            print_reason = "Отпуск очередной"
        elif reason == "Э":
            print_reason = "Отпуск учебный"
        elif reason == "Р":
            print_reason = "Отпуск по беремености"
        elif reason == "А":
            print_reason = "Отпуск за свой счет"
        elif reason == "Ж":
            print_reason = "Пенсионный/уход за детьми"
        elif reason == "Д":
            print_reason = "Донорский день"
        elif reason == "М":
            print_reason = "Медкомиссия"
        elif reason == "Б":
            print_reason = "Больничный"
        elif reason == "К":
            print_reason = "Командировка"
        else:
            print_reason ="неизвестная причина"

        return print_reason
    
    def print_period(start_day, final_day):

        if int(start_day) != int(final_day):
            period = f"{int(start_day):02.0f}.{int(month):02.0f}-{int(final_day):02.0f}.{int(month):02.0f}.{int(year)}"
            
        elif int(start_day) == int(final_day):
            period = f"{int(final_day):02.0f}.{int(month):02.0f}.{int(year)}"
        
        else:
            period = f"Неизвестный период"
        
        return period
    
    def print_cvalification(tabel): 
        cvalification = all_data["шифр"][str(profession_code)]["Табельный"][tabel]["разряд"]
        return cvalification
    
    def create_list_for_write_xls():
        list_for_write_xls = []

        for personal_number in tabels:
            substitutes_list = eval(substitutes["DEFAULT"][f"{profession_code},{personal_number}"])

            for item in substitutes_list:
                list_for_write_xls.append((
                    (f"{print_name(item[0])} таб. {item[0]}"),
                    (f"{profession_name},{print_cvalification(item[0])} разряд"),
                    (f"{print_reason(item[1])}"),
                    (f"{print_period(item[2],item[3])}"),
                    (f"{print_name(str(item[4]))}, таб {item[4]}"),
                    (f"{profession_name},{print_cvalification(str(item[4]))} разряд"),
                    (f"{tarif[str(profession_code)][print_cvalification(item[0])]} ")
                                    ))

        return list_for_write_xls

    return create_list_for_write_xls()


def write_to_file_string(profession_code = "87100" ):
    workbook =xlwt.Workbook()
    # Получать рабочий лист
    worksheet = workbook.add_sheet('form')
    # считаем количество строк которые требуется создать
    number_of_rows = len(load_data_and_create_list(profession_code))
    # считаем количество строк которые нужно создать в документе
    # количество строк в замещении делим на 15(количество позиций возможные в документе)
    # округляем до большего
    count = math.ceil(number_of_rows/11)*40
    create_file(worksheet=worksheet,count=count)
    
    # передаем информацию для записи
    list_for_write = load_data_and_create_list()
    
    def write_row(start_row,start_column,count,value):
        #sheet.merge(top_row, bottom_row, left_column, right_column)

        # записываем порядковый номер:
        worksheet.merge(start_row,start_row+1,start_column,start_column, set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        worksheet.write(start_row, start_column,str(count), set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

        # записываем фамилию имя замещаемого:
        worksheet.merge(start_row,start_row,start_column+1,start_column+2, set_style(bordleft=2,bordright=2,bordtop=2))
        worksheet.write(start_row, start_column+1,value[0], set_style(ahorz=0x02,bordleft=2,bordtop=2))

        # записываем профессию и разряд
        worksheet.merge(start_row+1,start_row+1,start_column+1,start_column+2, set_style(bordleft=2, bordright=2,bordbottom=2))
        worksheet.write(start_row+1, start_column+1,value[1], set_style(ahorz=0x02,bordleft=2, bordright=2,bordbottom=2))

        # записываем причину отсутствия
        worksheet.merge(start_row,start_row,start_column+3,start_column+4, set_style(bordleft=2,bordright=2,bordtop=2))
        worksheet.write(start_row, start_column+3,value[2], set_style(ahorz=0x02,bordleft=2,bordtop=2))

        # записываем период отсутствия
        worksheet.merge(start_row+1,start_row+1,start_column+3,start_column+4, set_style(bordleft=2, bordright=2,bordbottom=2))
        worksheet.write(start_row+1, start_column+3,value[3], set_style(ahorz=0x02,bordleft=2, bordright=2,bordbottom=2))

        # записываем тариф
        worksheet.merge(start_row,start_row+1,start_column+5,start_column+5, set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        worksheet.write(start_row, start_column+5,value[-1], set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

        # записываем фамилию замещающего
        worksheet.merge(start_row,start_row,start_column+6,start_column+8, set_style(bordleft=2, bordright=2,bordtop=2))
        worksheet.write(start_row, start_column+6,value[4], set_style(ahorz=0x02,bordleft=2,bordtop=2))

        # записываем профессию и разряд
        worksheet.merge(start_row+1,start_row+1,start_column+6,start_column+8, set_style(bordleft=2, bordright=2,bordbottom=2))
        worksheet.write(start_row+1, start_column+6,value[5], set_style(ahorz=0x02,bordleft=2, bordright=2,bordbottom=2))
        
        # записываем процент оплаты от тарифа
        worksheet.merge(start_row,start_row+1,start_column+9,start_column+9, set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        worksheet.write(start_row, start_column+9,f"{procent[str(profession_code)]}%", set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

        # согласие на исполнение(обьединение ячеек)
        worksheet.merge(start_row,start_row+1,start_column+10,start_column+10, set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        worksheet.write(start_row, start_column+10,"", set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        
        # окончательный размер оплаты(обьединение ячеек)
        worksheet.merge(start_row,start_row+1,start_column+11,start_column+11, set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        worksheet.write(start_row, start_column+11,"", set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))
        




    def write_file():
        # Информация для заполнения первой строниы(13 строка на ней заканчивается форма)
        start_row = 13
        start_column = 1
        # считаем количество строк
        end_of_count = len(list_for_write)
        row_count = 0
        for count in range(0,end_of_count):
            if count >10 and count%11==0:
                 start_row+=18
                 value = list_for_write[count]
                 write_row(start_row+row_count,start_column,count+1,value)
                 row_count+=2
            else:
                value = list_for_write[count]
                write_row(start_row+row_count,start_column,count+1,value)
                row_count+=2
            
        workbook.save(f'data\\199_{month}_{year}.xls')
    write_file()
    
if __name__ == "__main__":
    write_to_file_string("87100")
    




