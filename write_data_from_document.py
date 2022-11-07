import json
import xlwt
import configparser
import math

from create_form import create_file
from create_form import set_style

# входные данные
profession_code = 87100
month = "03"
year = "22"
tarif = {"87100":{6:9798,5:8910,4:8105,3:7365},"87200":{6:9798,5:8910,4:8105,3:7365},"08300":{6:9798,5:8910,4:8105,3:7365}}
procent = {"87100":{"30"},"87200":{"30"},"08300":{"70"}}

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
    count = math.ceil(number_of_rows/15)*40
    create_file(worksheet=worksheet,count=count)
    
    # передаем информацию для записи
    list_for_write = load_data_and_create_list()
    print(list_for_write[0])
    
    def write_row(start_row,start_column,count,value):
        #sheet.merge(top_row, bottom_row, left_column, right_column)

        # записываем порядковый номер:
        worksheet.merge(start_row,start_row+1,start_column,start_column, set_style(borders_type=2))
        worksheet.write(start_row, start_column,str(count), set_style(ahorz=0x02,borders_type=2))

        # записываем фамилию имя замещаемого:
        worksheet.merge(start_row,start_row,start_column+1,start_column+2, set_style())
        worksheet.write(start_row, start_column+1,value[0], set_style(ahorz=0x02))

        # записываем профессию и разряд
        worksheet.merge(start_row+1,start_row+1,start_column+1,start_column+2, set_style())
        worksheet.write(start_row+1, start_column+1,value[1], set_style(ahorz=0x02))

        # записываем причину отсутствия
        worksheet.merge(start_row,start_row,start_column+3,start_column+4, set_style())
        worksheet.write(start_row, start_column+3,value[2], set_style(ahorz=0x02))

        # записываем период отсутствия
        worksheet.merge(start_row+1,start_row+1,start_column+3,start_column+4, set_style())
        worksheet.write(start_row+1, start_column+3,value[3], set_style(ahorz=0x02))

        # записываем тариф
        worksheet.merge(start_row,start_row+1,start_column+5,start_column+5, set_style())
        worksheet.write(start_row, start_column+5,value[-1], set_style(ahorz=0x02))

        # записываем фамилию замещающего
        worksheet.merge(start_row,start_row,start_column+6,start_column+8, set_style())
        worksheet.write(start_row, start_column+6,value[4], set_style(ahorz=0x02))

        # записываем профессию и разряд
        worksheet.merge(start_row+1,start_row+1,start_column+6,start_column+8, set_style())
        worksheet.write(start_row+1, start_column+6,value[5], set_style(ahorz=0x02))












    value = list_for_write[0]
    write_row(13,1,1,value)
    

    workbook.save("test.xls")


if __name__ == "__main__":
    # print(load_data_and_create_list("87100"))
    write_to_file_string("87100")




