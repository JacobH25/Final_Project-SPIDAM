# upload_file.py
# Programmer Name: Jacob Hensley
# File Created: 4/20/2024

# import easygui for opening File Explorer
import easygui as eg


# upload_file function
def upload_file():
    # Initializes file as file selected by user via File Explorer
    file = eg.fileopenbox()
    # returns selected file
    return file

