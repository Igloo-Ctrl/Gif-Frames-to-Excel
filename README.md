# Images-to-Excel
A programmatic way of converting the RGB values of each individual pixel of an image into data, creating and configuring an Excel document and inputting the data. The script also creates a unique folder for the process and writes complementary VBA macros to faciliate the colouring.

![image](https://user-images.githubusercontent.com/107010803/205056554-e9f4eeee-58f0-4c6d-b2fe-12a11525db00.png)

Note: the colouring and formatting of the Excel file was done via VBA macros.

# What Does It Do?
1. The user inputs the filepath of their desired image
2. A check is done for the "images" folder in the current directory, if it isn't found, one is created
3. Validates the filepath to see if it exists and it is an image that can be processed
4. Creates a unique folder for the entire request
5. Grabs the RGB values of the image and stores them into a text document named "rgb.txt"
6. Creates an Excel workbook and configures it appropriately
7. Writes case specific VBA macros for use in resizing the Excel sheet and colouring it
