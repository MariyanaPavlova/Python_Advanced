# def operate(sign, *args):
#     if sign in ('+', '-'):
#         result = 0
#     else:
#         result = 1
#
#     if sign == '+':
#         for el in args:
#             result += el
#     elif sign == '-':
#         for el in args:
#             result -= el
#     elif sign == '*':
#         for el in args:
#             result *= el
#     elif sign == '/':
#         for el in args:
#             result /= el
#
#     return result
#
# print(operate("*", 3, 4))

from functools import reduce

def operate(sign, *args):
    result = reduce(lambda x, y: eval(f"{x} {sign} {y}"), args) # събира първите 2 после резултата с 3тото и т.н    return result

print(operate("+", 1,2,3))