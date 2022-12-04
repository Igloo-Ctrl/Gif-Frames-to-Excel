from PIL import Image, GifImagePlugin
import os

def create_directories():
    directory_names = ["gifs", "splits"]
    created_count = 0
    print(f'\nAttempting to create folders in "{os.getcwd()}"')
    for name in directory_names:
        try:
            os.mkdir(name)
            print(f'Successfully created the "{name}" directory.')
            created_count += 1
        except FileExistsError:
            print(f'The "{name}" directory already exists. Skipping.')
    print(f"{created_count}/2 folders created.")


def choose_gif_from_directory():
    current_files = os.listdir("gifs")
    if len(current_files) != 0:
        print("I found the following files:")
        for i in enumerate(current_files):
            print(f"{i[0] + 1}. {current_files[i[0]]}")
        user_input = input("\nType in the corresponding number to select a gif.\n")
        if current_files[int(user_input) - 1]:
            print("Boo!")
    else:
        print('No files found, please move a GIF into the "gifs" folder.')

def help_me():
    print("\n(Create Folders) - Creates the necessary folders to store GIFs and their splits\n"
          "(Split GIF) - Splits a GIF into its keyframes\n"
          "(Create and Configure Excel File) - Creates an Excel file and the necessary amount of sheets")

def split_gif():
    choose_gif_from_directory()

def create_and_configure_excel_document():
    pass

def main():
    user_input = input("Welcome to my humble program, please select an option by entering its corresponding number.\n"
          "1. Create Folders\n2. Split GIF\n3. Create & Configure Excel File\n4. Help\n\n> ")
    if user_input in possible_entries:
        possible_entries[user_input]()
    else:
        print("Invalid input.")

possible_entries = {
    "1": create_directories,
    "2": split_gif,
    "3": create_and_configure_excel_document,
    "4": help_me
}

main()