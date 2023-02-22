import sys
from io import StringIO

input_1 = '''4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)
'''
input_2 = '''5
3
(1, 1)
(2, 4)
(4, 1)
'''

sys.stdin = StringIO(input_1)

size = int(input())
bombs_count = int(input())
field = [[0] * size for _ in range(size)]


def is_valid_position(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return False
    return True


def play(matrix, bomb_coords):
    coords = bomb_coords.split(', ')
    row = int(coords[0])
    col = int(coords[1])

    matrix[row][col] = '*'

    if is_valid_position(size, row, col + 1):
        if matrix[row][col + 1] != "*":
            matrix[row][col + 1] += 1
    if is_valid_position(size, row + 1, col):
        if matrix[row + 1][col] != "*":
            matrix[row + 1][col] += 1
    if is_valid_position(size, row + 1, col + 1):
        if matrix[row + 1][col + 1] != "*":
            matrix[row + 1][col + 1] += 1

    if is_valid_position(size, row, col - 1):
        if matrix[row][col - 1] != "*":
            matrix[row][col - 1] += 1
    if is_valid_position(size, row - 1, col):
        if matrix[row - 1][col] != "*":
            matrix[row - 1][col] += 1
    if is_valid_position(size, row - 1, col - 1):
        if matrix[row - 1][col - 1] != "*":
            matrix[row - 1][col - 1] += 1

    if is_valid_position(size, row + 1, col - 1):
        if matrix[row + 1][col - 1] != "*":
            matrix[row + 1][col - 1] += 1
    if is_valid_position(size, row - 1, col + 1):
        if matrix[row - 1][col + 1] != "*":
            matrix[row - 1][col + 1] += 1


for _ in range(bombs_count):
    bomb = input()
    play(field, bomb[1:-1])

for f in field:
    print(*f)