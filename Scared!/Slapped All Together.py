from PIL import Image, GifImagePlugin
import os
from os.path import exists


def create_directories():
    directory_names = ["gifs", "images"]
    created_count = 0
    print(f'Attempting to create folders in "{os.getcwd()}".')
    for name in directory_names:
        try:
            os.mkdir(name)
            print(f'Successfully created the "{name}" directory.')
            created_count += 1
        except FileExistsError:
            print(f'The "{name}" directory already exists. Skipping.')
    print(f"\n{created_count}/2 folders created.")


def check_directory_for_images():
    current_files = os.listdir("images")
    if len(current_files) != 0:
        print("\nI found the following files:")
        for i in enumerate(current_files):
            print(f"{i[0] + 1}. {current_files[i[0]]}")
        while True:
            user_input = input("\nType in the corresponding number to select a image: ")
            try:
                if current_files[int(user_input) - 1]:
                    print("Boo!")
            except IndexError:
                print("\nInvalid input. Please try again.")
    else:
        blank_input = input('No files found in the "images" folder. Make sure there is a at least one '
                            'and press enter to try again.')
        check_directory_for_images()


def split_gif():
    check_directory_for_images()


def create_and_configure_excel_document():
    pass


def process_image():
    pass


def process_gif():
    pass


def check_for_directories():
    directory_names = ["gifs", "images"]
    exist_count = 0
    for name in directory_names:
        if exists(name):
            exist_count += 1
    if exist_count == 2:
        print("All folders present.\n")
    else:
        print("One or more folders are missing, let me fix that.\n")
        create_directories()


def image_or_gif():
    while True:
        user_input = input("Would you like to process an image or gif? ").lower()
        if user_input == "image":
            check_directory_for_images()
        elif user_input == "gif":
            print("Not yet implemented.")
        else:
            print("Invalid input.")


def main():
    print("Howdy stranger, I'm here to help you add images or GIFs into Excel. Let's get a move on, shall we?")
    print("First, let me check to see if you have all your initial folders setup...")
    check_for_directories()
    image_or_gif()


possible_entries = {
    "image": process_image,
    "gif": process_gif
}

if __name__ == '__main__':
    main()
