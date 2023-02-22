try:
    with open('text_file.txt') as file:
        print('File found!')
except FileNotFoundError:
    print('File not found')


import json

file = open("a.json")
my_dict = json.load(file)
print(type(my_dict))