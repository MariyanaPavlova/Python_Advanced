def get_next_posit(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col

n = int(input())
commands = input().split()

matrix = []

miner_row = 0
miner_col = 0
total_coal = 0

for row in range(n):
    row_el = input().split()
    matrix.append(row_el)

    for col in range(n):
        el = row_el[col]
        if el == "s":
            miner_row = row
            miner_col = col
        elif el == "c":
            total_coal +=1

game_over = False

for command in commands:
    next_row, next_col = get_next_posit(command, miner_row, miner_col)

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        continue

    miner_row, miner_col = next_row, next_col
    if matrix[miner_row][miner_col] == "c":
        matrix[miner_row][miner_col] = '*'
        total_coal -= 1

        if total_coal == 0:
            break
    elif matrix[miner_row][miner_col] == "e":
        game_over = True
        break

if total_coal == 0:
    print(f'You collected all coal! ({miner_row}, {miner_col})')
elif game_over:
    print(f'Game over! ({miner_row}, {miner_col})')
else:
    print(f'{total_coal} pieces of coal left. ({miner_row}, {miner_col})')

'''
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *

Game over! (1, 3)
'''

'''
4
up right right right down
* * * e
* * c *
* s * c
* * * *

You collected all coal! (2, 3)
'''

'''
6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *

3 pieces of coal left. (5, 0)

'''