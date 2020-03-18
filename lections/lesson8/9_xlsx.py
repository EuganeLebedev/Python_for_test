import openpyxl

workbook = openpyxl.load_workbook(filename='test.xlsx')

sheet = workbook.active
print(sheet['A2'].value)
print(sheet['B3'].value)

for i in sheet['A1:A3']:
    print(i[0].value)
for i in sheet['A1:B3']:
    print(i[0].value, ' ',  i[1].value)
