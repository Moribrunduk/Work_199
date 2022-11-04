# coding:utf-8
import xlwt
import time
 
i = 0
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
# Если возникает ошибка: Исключение: Попытка перезаписать ячейку: sheetname = 'sheet1' rowx = 0 colx = 0
 # Необходимо добавить: cell_overwrite_ok = True)
 # Это вызвано многократным использованием ячейки
 
while i < 64:
         # Создать шрифт для стиля
    font = xlwt.Font()
 
         # Тип шрифта
    font.name = 'name Times New Roman'
         # Цвет шрифта 
    font.colour_index = i
         # Размер шрифта, 11 - размер шрифта, 20 - единица измерения
    font.height = 20 * 11
         # Жирный шрифт
    font.bold = False
         # Нижнее подчеркивание
    font.underline = True
         # курсив
    font.italic = True
 
         # Установить выравнивание ячеек
    alignment = xlwt.Alignment()
         # 0x01 (выровнен по левому краю), 0x02 (выровнен по центру в горизонтальном направлении), 0x03 (выровнен по правому краю)
    alignment.horz = 0x02
         # 0x00 (выровнен по верху), 0x01 (выровнен по центру в вертикальном направлении), 0x02 (выровнен по низу)
    alignment.vert = 0x01
 
         # Установить автоматический перенос строк
    alignment.wrap = 1
 
         # Установить границу
    borders = xlwt.Borders()
         # Тонкая сплошная линия: 1, маленькая толстая сплошная линия: 2, тонкая пунктирная линия: 3, средняя тонкая пунктирная линия: 4, большая толстая сплошная линия: 5, двойная линия: 6, тонкая пунктирная линия: 7
         # Большая толстая пунктирная линия: 8, тонкая пунктирная линия: 9, толстая пунктирная линия: 10, тонкая двойная пунктирная линия: 11, толстая двойная пунктирная линия: 12, наклонная пунктирная линия: 13
    borders.left = 1
    borders.right = 2
    borders.top = 3
    borders.bottom = 4
    borders.left_colour = i
    borders.right_colour = i
    borders.top_colour = i
    borders.bottom_colour = i
 
         # Установите ширину столбца, один китайский равен двум, английский равен двум символам, 11 - это количество символов, а 256 - это единица измерения
    sheet.col(1).width = 11 * 256
 
         # Установить цвет фона
    pattern = xlwt.Pattern()
         # Установить режим цвета фона
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
         # фоновый цвет 
    pattern.pattern_fore_colour = i
 
         # Инициализировать стиль
    style0 = xlwt.XFStyle()
    style0.font = font
 
    style1 = xlwt.XFStyle()
    style1.pattern = pattern
 
    style2 = xlwt.XFStyle()
    style2.alignment = alignment
 
    style3 = xlwt.XFStyle()
    style3.borders = borders
 
         # Установить текстовый режим
    font.num_format_str = '#,##0.00'
 
         sheet.write (я, 0, u'font ', style0)
         sheet.write (i, 1, u'background ', style1)
         sheet.write (i, 2, u'alignment ', style2)
         sheet.write (i, 3, u'border ', style3)
 
         # Объединить ячейки, объединить столбцы с 4 по 5 из строк со 2 по 4
         sheet.write_merge (2, 4, 4, 5, u'merge ')
    i = i + 1
 
book.save('test_file' + time.strftime("%Y%m%d%H%M%S") + '.xls')