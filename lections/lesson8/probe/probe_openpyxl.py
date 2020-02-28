import openpyxl

wb = openpyxl.Workbook()

ws = wb.active

ws['A1'] = 24

ws.append([1, 2, 3, 4])

wb.save('xlsx_probe.xlsx')
