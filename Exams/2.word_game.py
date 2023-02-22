def get_next_posit(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


name = input()
n = int(input())
output_name = name

matrix = []
player_pos = []


for i in range(n):
    row_data = list(input())
    if 'P' in row_data:
        player_pos = [i, row_data.index("P")]
    matrix.append(row_data)

pl_row, pl_col = player_pos

command_count = int(input())

for i in range(command_count):
    command = input()

    next_row, next_col = get_next_posit(command, pl_row, pl_col) # взимаме новите коорд.

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        if output_name:
            output_name = output_name[:-1:]
            continue
        else:
            pass

    if matrix[next_row][next_col] != "-":
        output_name += matrix[next_row][next_col]

    matrix[pl_row][pl_col] = "-"  # чистим старата поз
    #matrix[next_row][next_col] = "-" # чистим и новата поз.- Ненужно 49р.пак я променя

    pl_row, pl_col = next_row, next_col # презаписваме позицията
    matrix[pl_row][pl_col] = "P" # слагаме играча на новата поз с презап.коорд

print(output_name)
for x in matrix:
    print(*x, sep="")

"""
Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right

HelloMark
----
---P
-l-y
--e-
"""

'''
Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left

Initialr
-----
P----
---a-
--S--
z--t-
'''