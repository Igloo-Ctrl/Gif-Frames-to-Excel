from PIL import Image
import os
from os.path import exists
import uuid

# enter the file path to your image here, for example, /Users/johndoe/Downloads/cat.png
filepath = "D:\Downloads\grinch.jpg"


class Variables:
    filepath = ""
    filename = ""


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
    image_width, image_height = open_image.size[0], open_image.size[1]
    # rgb_image = open_image.convert("rgb")

    data_string = ""
    for i in range(image_width):
        for j in range(image_height):
            data_string += f"{open_image.getpixel((i, j))[0]}, {open_image.getpixel((i, j))[1]}, " \
                           f"{open_image.getpixel((i, j))[2]}\n"

    with open(f"{Variables.filepath}/rgb_text.txt", "w") as f:
        f.write(data_string)
        print(f"RGB text file created.")


def main():
    check_for_folder()


if __name__ == '__main__':
    main()