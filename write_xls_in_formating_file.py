from xmlrpc.client import TRANSPORT_ERROR
from xlutils.copy import copy
import xlrd
from xlrd import *
import xlwt 
book = copy(open_workbook('199.xls',on_demand=True,formatting_info=True))
worklist = book.get_sheet(0).write(0,0, "foo")
book.save('book2.xls')