from openpyxl import Workbook

amount_of_sheets = 57
excel_filename = "test.xlsx"


def create_work_book():
    """creates a workbook by the name specified above and creates as many sheets as stated above
    deletes the first sheet and then saves everything"""
    wb = Workbook()
    wb.save(filename=excel_filename)
    for i in range(1, amount_of_sheets + 1):
        wb.create_sheet(title=f"Frame {i}")
    del wb["Sheet"]
    wb.save(filename=excel_filename)


if __name__ == '__main__':
    create_work_book()
