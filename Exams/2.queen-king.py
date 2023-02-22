def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

matrix = []
n = 8

for i in range(n):
    matrix.append(input().split())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up-right": (-1, 1),
    "up-left": (-1, -1),
    "down-right": (1, 1),
    "down-left": (1, -1)
}
queens = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "Q":
            for direc in directions:
                next_row = row + directions[direc][0]
                next_col = col + directions[direc][1]

                while is_in_range(next_row, next_col, n):
                    if matrix[next_row][next_col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        queens.append([row, col])
                        break
                    next_row += directions[direc][0]
                    next_col += directions[direc][1]
if queens:
    [print(x) for x in queens]
else:
    print('The king is safe!')