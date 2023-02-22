def even_odd(*args):
    if args[-1] == "even":
        result = [int(x) for x in args[0:-1] if x % 2 == 0]
    else:
        result = [int(x) for x in args[0:-1] if x % 2 != 0]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

--------
def even_odd(*args):
    command = args[-1]
    if command == 'even':
        return list(filter(lambda x: x%2 == 0, args[0:-1]))
    else: #може и без else
        return list(filter(lambda x: x%2 != 0, args[0:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, 'even'))

-------
def is_even(num):
    return num %2 ==0

def is_odd(num):
    return not is_even(num)

def even_odd(*args):
    command = args[-1]
    numb = args[0:-1]

    if command == 'even':
        return list(filter(is_even, numb))
    elif command == 'odd':
        return list(filter(is_odd, numb))


print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
