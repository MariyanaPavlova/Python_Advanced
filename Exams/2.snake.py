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

matrix = []
food = 0
snake_pos = []
B = []


for i in range(n):
    row_data = list(input())
    if 'S' in row_data:
        snake_pos = [i, row_data.index("S")]
    if 'B' in row_data:
        B.append([i, row_data.index("B")])
    matrix.append(row_data)

command = input()
st_row, st_col = snake_pos
game_over = False

while command:

    matrix[st_row][st_col] = "."
    next_row, next_col = get_next_posit(command, st_row, st_col)

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        game_over = True
        break

    if matrix[next_row][next_col] == 'B':
        coord = [next_row, next_col]
        matrix[next_row][next_col] = '.'
        for i in B:
            if i == coord:
                B.remove(coord)
        for i in B:
            a = i[0]
            b = i[1]
            matrix[a][b] = '.'
            B.remove([a, b])
            next_row, next_col = a, b

    elif matrix[next_row][next_col] == '*':
        food += 1
    else:
        matrix[next_row][next_col] = '.'

    matrix[next_row][next_col] = "S"

    st_row, st_col = next_row, next_col

    if food == 10:
        break
    command = input()

if game_over:
    print('Game over!')
    print(f'Food eaten: {food}')
else:
    print(f'You won! You fed the snake.')
    print(f'Food eaten: {food}')

for x in matrix:
    print(*x, sep="")

'''
6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left

Game over!
Food eaten: 1
----..
----.-
------
------
--.---
--.---

'''


'''
7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down


You won! You fed the snake.
Food eaten: 10
--....-
--.----
--...--
---..--
---S---
---*---
---*---

'''