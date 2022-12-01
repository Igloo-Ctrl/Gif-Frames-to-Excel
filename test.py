# from openpyxl import Workbook, load_workbook
#
# workbook = load_workbook(filename='hello_world.xlsx')
#
# print(workbook.active)
# workbook.active = 0
# print(workbook.active)


count = 0
with open("frames/frame_1.txt") as f:
    data = f.readlines()
    for i in data:
        count += 1
print(count)
