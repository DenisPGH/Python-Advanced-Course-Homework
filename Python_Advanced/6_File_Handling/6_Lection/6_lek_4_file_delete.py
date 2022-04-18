import os

try:
    os.remove("my_first_file.txt")
    print("file deleted")
except FileNotFoundError:
    print('File already deleted!')