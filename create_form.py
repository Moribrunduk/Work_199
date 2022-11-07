import xlwt

def set_style(name="Arial", height = 10*20, bold=False, ahorz=0x01, avert=0x01,awrap=0,bordleft=0, bordright=0,bordtop=0,bordbottom=0):
    style = xlwt.XFStyle()  # Шаблон инициализации
    # Установить выравнивание ячеек
    alignment = xlwt.Alignment()
         # 0x01 (выровнен по левому краю), 0x02 (выровнен по центру в горизонтальном направлении), 0x03 (выровнен по правому краю)
    alignment.horz = ahorz
         # 0x00 (выровнен по верху), 0x01 (выровнен по центру в вертикальном направлении), 0x02 (выровнен по низу)
    alignment.vert = avert
         # Установить автоматический перенос строк
    alignment.wrap = awrap

    borders = xlwt.Borders()
         # Тонкая сплошная линия: 1, маленькая толстая сплошная линия: 2, тонкая пунктирная линия: 3, средняя тонкая пунктирная линия: 4, большая толстая сплошная линия: 5, двойная линия: 6, тонкая пунктирная линия: 7
         # Большая толстая пунктирная линия: 8, тонкая пунктирная линия: 9, толстая пунктирная линия: 10, тонкая двойная пунктирная линия: 11, толстая двойная пунктирная линия: 12, наклонная пунктирная линия: 13
    borders.left = bordleft
    borders.right = bordright
    borders.top = bordtop
    borders.bottom = bordbottom

    font = xlwt.Font()      # Создайте шрифт для шаблона
    font.name = name        # Определите определенные шрифты

    font.bold = bold        # Определить, жирный
    font.color_index = 4    # Определите цвет шрифта
    font.height = height    # Определите высоту шрифта
    style.alignment = alignment #определяем выравнивание
    style.borders = borders  # определяем границы  

    style.font = font       # Наконец определите пользовательские шрифты, определенные в стиле
    return style

    


# создаем документ
workbook =xlwt.Workbook()
# Получать рабочий лист
# worksheet = workbook.add_sheet('form')

def write_excel(worksheet,start_row = 0):
    # редактируемые данные
    
    month_with_sfx ="марта"
    year = '2022'
    number_vedom = "171"
    month = "март"

    #Данные стандартной таблицы
    value_1 = 'АО  "ПО "СЕВМАШ"'
    worksheet.write(start_row, 1, value_1, set_style())

    value_2 = 'Цех (отдел)      НИТИЦ'
    worksheet.write(start_row+2, 1, value_2, set_style())

    value_3 = 'СОГЛАШЕНИЕ-РАСЧЕТ ОПЛАТЫ' 
    worksheet.write(start_row+4, 1, value_3, set_style())

    value_4 = f'от  01 {month_with_sfx} {year} г. № 25.17/{number_vedom}    за {month} {year} г.'
    worksheet.write(start_row+6, 1, value_4, set_style())

    value_5 = '"ЗА ИСПОЛНЕНИЕ ОБЯЗАННОСТЕЙ ВРЕМЕННО ОТСУТСТВУЮЩЕГО РАБОТНИКА"'
    worksheet.write(start_row, 4, value_5, set_style())

    value_6 = "Руководствуясь положение 56.61-1.01.014.-2020, возложить частичное исполнение обязанностей временно"
    worksheet.write(start_row+1, 4, value_6, set_style())

    value_7 = 'отсутствующего работника с установлением оплаты видом 199 ведомостью РВО на следующих работников:'
    worksheet.write(start_row+2, 4, value_7, set_style())

    value_8 = '№ п/п'
    #sheet.merge(top_row, bottom_row, left_column, right_column)
    worksheet.merge(start_row+8,start_row+8+4,1,1, set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+8, 1, value_8, set_style(awrap=1, ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_9 = 'Отсутствующий работник, вакантная должность'
    worksheet.merge(start_row+8,start_row+8,2,6,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+8, 2, value_9, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_10 = 'Работник исполняющий обязанности временно отсутствующего'
    worksheet.merge(start_row+8,start_row+8,7,12,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+8, 7, value_10, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_11 = 'Фамилия И.О., таб. №	'
    worksheet.merge(start_row+9,start_row+10,2,3,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 2, value_11, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_12 = 'Профессия (должность),  разряд'
    worksheet.merge(start_row+11,start_row+12,2,3,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+11, 2, value_12, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_13 = 'Причина отсутствия'
    worksheet.merge(start_row+9,start_row+10,4,5,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 4, value_13, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_14 = 'Период отсутствия'
    worksheet.merge(start_row+11,start_row+12,4,5,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+11, 4, value_14, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_15 = 'Тариф (оклад), руб'
    worksheet.merge(start_row+9,start_row+12,6,6,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 6, value_15, set_style(awrap=1,ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_16 = 'Фамилия И.О., таб. №'
    worksheet.merge(start_row+9,start_row+10,7,9,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 7, value_16, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_17 = 'Профессия (должность), разряд'
    worksheet.merge(start_row+11,start_row+12,7,9,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+11, 7, value_17, set_style(ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_18 = 'Предварительный % оплаты от тарифа (оклада) отсутствующего'
    worksheet.merge(start_row+9,start_row+12,10,10,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 10, value_18, set_style(awrap=1,ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    value_19 = 'Согласие на исполнение, подпись, дата'
    worksheet.merge(start_row+9,start_row+12,11,11,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 11, value_19, set_style(awrap=1,ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    
    value_20 = 'Окончательный размер оплаты, руб.'
    worksheet.merge(start_row+9,start_row+12,12,12,set_style(bordleft=2, bordright=2,bordtop=2,bordbottom=2))
    worksheet.write(start_row+9, 12, value_20, set_style(awrap=1,ahorz=0x02,bordleft=2, bordright=2,bordtop=2,bordbottom=2))

    main_person = 'Начальник НИТИЦ'
    main_person_name = 'А.И. Власов'
    botiz = 'Начальник БОТиЗ'
    botiz_name = 'Н.А.Львова'
    
    #считаем длину строки без нижнего подчеркивания
    x_value_21 = len(f'{main_person}/{main_person_name} / Мастер (руководитель работ)/{botiz}/{botiz_name}/')
    #Собираем строку
    value_21 =f'{main_person}{int((142-x_value_21)/4)*"_"}/{main_person_name} / Мастер (руководитель работ){int((135-x_value_21)/4)*"_"}/{int((135-x_value_21)/4)*"_"}{botiz}{int((135-x_value_21)/4)*"_"}/{botiz_name}/'
    worksheet.write(start_row+37, 1, value_21, set_style(ahorz=0x01))

    value_22 =f'{34*" "}подпись,дата{80*" "}подпись,дата{56*" "}подпись,дата'
    worksheet.write(start_row+38, 1, value_22, set_style(ahorz=0x01))
    

    value_23 = 'ф.56.61.70'
    worksheet.write(start_row+39, 12, value_23, set_style(ahorz=0x03))

    # форматирование таблицы
    col_width = [987,1206,2889,4425,2669,1938,2048,2340,2340,2669,4169,3547,4059,950] #стянуто из рабочего файла
    col = 0
    for item in col_width:
        worksheet.col(col).width = item
        col+=1

def create_file(worksheet,count=40):
     page_breaks = []
     for item in range(0,count,40):
          write_excel(worksheet,start_row=item)
          page_breaks.append((item+40,0,0))
          worksheet.horz_page_breaks = page_breaks
     worksheet.set_portrait(False)
     

if __name__ == '__main__':
     create_file()
     workbook.save("form.xls")
     