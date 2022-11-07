import json
import xlwt
import configparser

from create_form import create_file


workbook =xlwt.Workbook()
# Получать рабочий лист
worksheet = workbook.add_sheet('form')

create_file(worksheet=worksheet,count=40)
value_test =f'ТЕСТ'
worksheet.write(13, 2, value_test)
workbook.save("test.xls")

# входные данные
profession_code = 87100
month = "03"
year = "22"
tarif = {"87100":{6:9798,5:8910,4:8105,3:7365},"87200":{6:9798,5:8910,4:8105,3:7365},"08300":{6:9798,5:8910,4:8105,3:7365}}

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
                    (f"{profession_name},{print_cvalification(item[0])} разряд,"),
                    (f"{print_reason(item[1])}"),
                    (f"{print_period(item[2],item[3])}"),
                    (f"{print_name(str(item[4]))}, таб {item[4]}"),
                    (f"{profession_name},{print_cvalification(str(item[4]))} разряд"),
                    (f"{tarif[str(profession_code)][print_cvalification(item[0])]} ")
                                    ))

        return list_for_write_xls

    return create_list_for_write_xls()

def set_style():
    pass
def write_to_file_string(row,col,data):
    pass


if __name__ == "__main__":
    print(load_data_and_create_list("87100"))



