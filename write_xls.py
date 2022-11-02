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

# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet(f'199 для {profession_code}')


# font0 = xlwt.Font()
# font0.name = 'Times New Roman'
# font0.colour_index = 2
# font0.bold = True

# style0 = xlwt.XFStyle()
# style0.font = font0

# style1 = xlwt.XFStyle()
# style1.num_format_str = 'D-MMM-YY'

from xlrd import open_workbook
from xlutils.copy import copy
import xlwt

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # Шаблон инициализации
    # Установить выравнивание ячеек
    alignment = xlwt.Alignment()
         # 0x01 (выровнен по левому краю), 0x02 (выровнен по центру в горизонтальном направлении), 0x03 (выровнен по правому краю)
    alignment.horz = 0x02
         # 0x00 (выровнен по верху), 0x01 (выровнен по центру в вертикальном направлении), 0x02 (выровнен по низу)
    alignment.vert = 0x01
         # Установить автоматический перенос строк
    alignment.wrap = 1

    borders = xlwt.Borders()
         # Тонкая сплошная линия: 1, маленькая толстая сплошная линия: 2, тонкая пунктирная линия: 3, средняя тонкая пунктирная линия: 4, большая толстая сплошная линия: 5, двойная линия: 6, тонкая пунктирная линия: 7
         # Большая толстая пунктирная линия: 8, тонкая пунктирная линия: 9, толстая пунктирная линия: 10, тонкая двойная пунктирная линия: 11, толстая двойная пунктирная линия: 12, наклонная пунктирная линия: 13
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1

    font = xlwt.Font()      # Создайте шрифт для шаблона
    font.name = name        # Определите определенные шрифты

    font.bold = bold        # Определить, жирный
    font.color_index = 4    # Определите цвет шрифта
    font.height = height    # Определите высоту шрифта
    style.alignment = alignment #определяем выравнивание
    style.borders = borders # определяем границы  

    style.font = font       # Наконец определите пользовательские шрифты, определенные в стиле
    return style

# Напишитеexcel

def write_excel():
    # Прочитать одинexcelдокумент
    workbook = open_workbook('199.xls',on_demand=True,formatting_info=True)
    # из xlrd Преобразование объекта к xlwt 
    new_excel = copy(workbook)
    # Получать рабочий лист
    worksheet = new_excel.get_sheet(0)
    # Подготовьте контент для входа
    values = ['Воронов Е.М. \n таб. 479 разряд 5','отпуск \n 07.11.2022','Илюхин Ю.В.\n таб. 473 разряд 5','3000']

    for x in range(4,10,2):
        # xlwtСпособ написания объекта, параметры - это линия, столбец, значение соответственно
        worksheet.write(x, 1, values[0], set_style('Times New Roman', 9*20 ,False))
        worksheet.write(x, 5, values[1], set_style('Times New Roman', 9*20 ,False))
        worksheet.write(x, 7, values[2], set_style('Times New Roman', 9*20 ,False))
        worksheet.write(x, 14, values[3], set_style('Times New Roman', 9*20 ,False))
    
    

    # xlwtМетод сохранения объекта, затем покрыл оригиналexcel
    new_excel.save("book2.xls")


if __name__ == '__main__':
    write_excel()




