from PIL import Image
import os
from os.path import exists
import uuid


def check_for_folder():
    print(f'Checking "{os.getcwd()}" for "images" folder.')
    if exists("images"):
        print('"Images" folder found.')
    else:
        os.mkdir("images")
        print('"Images" folder not found. Creating.')
    prompt_filename()


# def validate_filepath():
#     if Variables.filepath == "":
#         exit('Filepath empty, please change the filepath in the class "Variables" to a valid path.')
#     else:
#         try:
#             Image.open(Variables.filepath)
#             process_image(Variables.filepath)
#         except IOError:
#             print("Invalid file type.")


def prompt_filename():
    user_input = input("Please enter the filepath of your image: ")
    if exists(user_input):
        try:
            Image.open(user_input)
            print("Valid file type. Proceeding.")
            create_and_move(user_input)
            # process_image(user_input)
        except IOError:
            print("Invalid file type.")
            prompt_filename()
    else:
        print(f'The file "{user_input}" does not exist.\n')


def create_and_move(filepath):
    # directory
    filename = os.path.basename(filepath)
    generated_filename = str(uuid.uuid4())
    os.mkdir(f"images/{generated_filename}")

    # saving a copy of the image
    image = Image.open(filepath)
    image.save(f"images/{generated_filename}/{filename}")
    print("Creating a folder for this process.")


def process_image(filepath):
    open_image = Image.open(filepath)
    image_width, image_height = open_image.size[0], open_image.size[1]
    # rgb_image = open_image.convert("rgb")

    data_string = ""
    for i in range(1, image_width):
        for j in range(1, image_height):
            data_string += f"{open_image.getpixel((j, i))[0]}, {open_image.getpixel((j, i))[1]}, " \
                           f"{open_image.getpixel((j, i))[2]}\n"

    with open(f"images/test.txt", "w") as f:
        f.write(data_string)
        print(f"test.txt complete!")


def main():
    check_for_folder()


if __name__ == '__main__':
    main()
