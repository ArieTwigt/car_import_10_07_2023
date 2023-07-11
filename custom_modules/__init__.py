import os

files_folders = os.listdir()

if "export" not in files_folders:
    print("Creating export folder")
    os.mkdir("export")