import os

try:
    os.remove("my_first_file.txt")
    print("Deleted")
except FileNotFoundError:
    print("File already deleted!")
