from PIL import Image
import os
from os.path import exists
import uuid
from openpyxl import Workbook, load_workbook

# enter the file path to your image here, for example, /Users/johndoe/Downloads/cat.png
# filepath = "D:\Downloads\grinch.jpg"
filepath = "/Users/ryanjones/Downloads/IMG_0929.jpeg"

class Variables:
    image_width = ""
    image_height = ""
    image_filepath = ""
    image_filename = ""
    excel_file_path = ""


def check_for_folder():
    print(f'Checking "{os.getcwd()}" for "images" folder.')
    if exists("images"):
        print('"Images" folder found.')
    else:
        os.mkdir("images")
        print('"Images" folder not found. Creating.')
    validate_filepath()


def validate_filepath():
    if filepath == "":
        exit('Filepath empty, please change the filepath at the top of this script to a valid location.')
    else:
        try:
            Image.open(filepath)
            print(f'Valid image found at "{filepath}". Proceeding.')
            create_and_move(filepath)
            process_image(filepath)
        except IOError:
            print("Invalid file type.")


def create_and_move(filepath):
    # directory
    Variables.filename = os.path.basename(filepath)
    generated_filename = str(uuid.uuid4())
    Variables.filepath = f"images/{generated_filename}"
    os.mkdir(Variables.filepath)

    # saving a copy of the image
    image = Image.open(filepath)
    image.save(f"images/{generated_filename}/{Variables.filename}")
    image.close()
    print("Creating a folder for this process and copying your image there.")


def process_image(filepath):
    open_image = Image.open(filepath)
    Variables.image_width, Variables.image_height = open_image.size[0], open_image.size[1]
    # rgb_image = open_image.convert("rgb")

    data_string = ""
    for i in range(Variables.image_width):
        for j in range(Variables.image_height):
            data_string += f"{open_image.getpixel((i, j))[0]}, {open_image.getpixel((i, j))[1]}, " \
                           f"{open_image.getpixel((i, j))[2]}\n"

    with open(f"{Variables.image_filepath}/rgb.txt", "w") as f:
        f.write(data_string)
        print(f"RGB text file created.")
    create_work_book()
def create_work_book():
    """creates a workbook by the name specified above and creates as many sheets as stated above
    deletes the first sheet and then saves everything"""
    wb = Workbook()
    wb.create_sheet(title=f"{Variables.image_filename}")
    del wb["Sheet"]
    Variables.excel_file_path = f"{Variables.image_filepath}/excel.xls"
    wb.save(Variables.excel_file_path)
    print("Excel Workbook created.")

def input_rbg_into_excel():
    workbook = load_workbook(Variables.excel_file_path)
    row, column = 1, 1
    sheet = workbook.active
    with open(f"rgb.txt", "r") as f:
        data = f.readlines()
        for i in data:
            if column > Variables.image_width:
                row += 1
                column = 1
            sheet.cell(column=column, row=row, value=i)
            column += 1

def main():
    check_for_folder()


if __name__ == '__main__':
    main()