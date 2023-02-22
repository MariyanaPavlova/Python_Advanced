from functools import reduce

import requests

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

# print(map(lambda x,y: int(x+y), ('1', '2', '3'))
# print(reduce(lambda x,y: x+y, [1, 2, 3]))

requests.get
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))