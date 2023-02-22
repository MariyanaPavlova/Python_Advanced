n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

command = input()
while not command == "END":
    command1 = command.split()
    com = command1[0]
    row, col, val = [int(x) for x in command1[1:]]

    if col < 0 or row >= n or col >= n or row < 0:
        print('Invalid coordinates')
        continue

    if com == "Add":
        matrix[row][col] += val
    elif com == "Subtract":
        matrix[row][col] -= val

    command = input()

for i in matrix:
    print(*i, sep=" ")


# *****
# def add(row_index: int, col_index: int, number: int):
#     matrix[row_index][col_index] += number
#
#
# def subtract(row_index: int, col_index: int, number: int):
#     matrix[row_index][col_index] -= number
#
#
# def check_indexes(row_index: int, col_index: int):
#     if 0 <= row_index < n and 0 <= col_index < n:
#         return True
#     print("Invalid coordinates")
#     return False
#
#
# def print_matrix():
#     for el in matrix:
#         print(*el)
#
#
# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(el) for el in input().split()])
#
# command = input()
#
# while not command == 'END':
#     action, row, col, num = command.split()
#     if check_indexes(int(row), int(col)):
#         if action == 'Add':
#             add(int(row), int(col), int(num))
#         elif action == 'Subtract':
#             subtract(int(row), int(col), int(num))
#
#     command = input()
# print_matrix()

