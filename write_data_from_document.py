import json
import xlwt


# with open("data\\all_data2.json", "r", encoding="utf-8") as file:
#         all_data = json.load(file)

# from xlutils.copy import copy 

# from xlrd import open_workbook

# workbook = copy(open_workbook('form.xls',formatting_info=True))
# w_sheet = workbook.get_sheet(0) 
# workbook.save("complited_file.xls")

from create_form import create_file
workbook =xlwt.Workbook()
# Получать рабочий лист
worksheet = workbook.add_sheet('form')

create_file(worksheet=worksheet,count=40)

value_test =f'ТЕСТ'
worksheet.write(13, 2, value_test)

workbook.save("test.xls")
