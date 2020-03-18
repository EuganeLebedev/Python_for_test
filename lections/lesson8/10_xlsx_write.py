import openpyxl

workbook = openpyxl.load_workbook(filename='test.xlsx')

sheet = workbook.active

sheet['B3'] = 'New Value!'

workbook.save(filename='result.xlsx')
