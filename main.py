from PIL import Image
import os

# folder contents
# folder_contents = os.listdir("ezgif-1-45bea6792c-gif-png")
folder_contents = os.listdir("120")

# ZE LOOP!!!
for image in enumerate(folder_contents):
    # open the image, convert to rgb and then load it
    scene_image = Image.open(f"ezgif-1-45bea6792c-gif-png/{image[1]}")
    rgb_image = scene_image.convert("RGB")
    load_image = scene_image.load()

    # image width and height
    image_width, image_height = scene_image.size[0], scene_image.size[1]

    # string to place all the data
    test_string = ""

    # nested for loop grab every pixel from the image, grab its specific rgb value and slap it into a document
    for i in range(1, image_width):
        for j in range(1, image_height):
            test_string += f"" \
                           f"{rgb_image.getpixel((j, i))[0]}, {rgb_image.getpixel((j, i))[1]}, {rgb_image.getpixel((j, i))[2]}-" \
                           f""
        test_string += "\n"

    # writes to document
    with open(f"frames/frame_{image[0] + 1}.txt", "w") as f:
        f.write(test_string)
        print(f"frame_{image[0] + 1}.txt complete!")
    break