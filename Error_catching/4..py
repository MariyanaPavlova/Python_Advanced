numbers_dictionary = {}

line = input()
while line != 'Search':
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = input()

line = input()
while line != "Remove":
    searched = line
    # value = numbers_dictionary.get(searched)
    # if not value:
    #     continue
    # print(numbers_dictionary[searched])
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dict")

    line = input()

print(numbers_dictionary)