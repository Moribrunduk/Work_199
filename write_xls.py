import configparser
from ctypes import alignment

config = configparser.ConfigParser()
config.read('temp.ini')
print(config['General']['for_summ'])     # -> "/path/name/"

profession_code = 87100

# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create
# with open('FILE.INI', 'w') as configfile:    # save
#     config.write(configfile)

# # рабочая часть файла
# data = eval(config['General']['for_summ'])
# print(data)


from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
# Напишитеexcel

def write_excel():
    # Прочитать одинexcelдокумент
    workbook = open_workbook('1.xls',on_demand=True,formatting_info=True)
    # из xlrd Преобразование объекта к xlwt 
    new_excel = copy(workbook)
    # Получать рабочий лист
    worksheet = new_excel.get_sheet(0)
    # Подготовьте контент для входа
    z = []
    for i in range (0,15):
          cwidth = worksheet.col(i).width
          print(f"{i}----- {cwidth}")
          z.append(cwidth)
    print(z)
    


if __name__ == '__main__':
    write_excel()




