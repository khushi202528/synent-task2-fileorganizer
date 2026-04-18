import os
import shutil

# take folder location
folder = input("Enter the folder location: ")

# get all items inside folder
items = os.listdir(folder)

for item in items:
    full_path = os.path.join(folder, item)

    # check if it is a file
    if os.path.isfile(full_path):

        # get extension in lowercase
        extension = item.split(".")[-1].lower()

        # decide folder name based on type
        if extension in ["jpg", "png", "jpeg", "gif"]:
            target_folder = "Image_Files"

        elif extension in ["pdf", "docx", "txt", "pptx"]:
            target_folder = "Document_Files"

        elif extension in ["mp4", "avi", "mkv"]:
            target_folder = "Video_Files"

        else:
            target_folder = "Other_Files"

        # create target folder if not exists
        new_folder_path = os.path.join(folder, target_folder)
        os.makedirs(new_folder_path, exist_ok=True)

        # move file to new folder
        shutil.move(full_path, os.path.join(new_folder_path, item))

print("All files have been sorted successfully!")