from openpyxl import Workbook, load_workbook

workbook = load_workbook(filename='hello_world.xlsx')

print(workbook.active)
workbook.active = 0
print(workbook.active)