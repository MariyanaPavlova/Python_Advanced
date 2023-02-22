def flights(*args):

    list_args = list(args)
    dict = {}

    for i in range(0, len(list_args), 2):
        if list_args[i] != "Finish":
            if list_args[i] not in dict:
                dict[list_args[i]] = list_args[i+1]
            else:
                dict[list_args[i]] += list_args[i+1]
        else:
            break
    return dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0))
