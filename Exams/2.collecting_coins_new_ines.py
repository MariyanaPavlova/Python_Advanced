def calc_position(ma, row, col): # поз.отива от др.страна
    if row < 0:
        row = len(ma) - 1
    if col < 0:
        col = len(ma) - 1
    if row >= len(ma):
        row = 0
    if col >= len(ma):
        col = 0
    return row, col

n = int(input())

matrix = []
player_pos = []

for row_i in range(n):
    row_data = input().split()
    if 'P' in row_data:
        player_pos = [row_i, row_data.index("P")]
    matrix.append(row_data)

player_path = []

coins = 0
is_winner = True
player_path.append(player_pos)

while coins < 100:

    command = input()

    curr_row, curr_col = player_pos
    if command == 'up':
        row, col = calc_position(matrix, curr_row-1, curr_col)
    elif command == 'down':
        row, col = calc_position(matrix, curr_row+1, curr_col)
    elif command == 'right':
        row, col = calc_position(matrix, curr_row, curr_col+1)
    elif command == 'left':
        row, col = calc_position(matrix, curr_row, curr_col-1)

    matrix[curr_row][curr_col] = "0"

    if matrix[row][col] == 'X':
        player_path.append(player_pos)
        is_winner = False
        coins //=2
        print(f"Game over! You've collected {coins} coins.")
        break

    coins += int(matrix[row][col])
    matrix[row][col] = "P"
    player_pos = [row, col]
    player_path.append(player_pos)

if is_winner:
    print(f"You won! You've collected {coins} coins.")
print('Your path:')
[print(x) for x in player_path]



'''
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right

You won! You've collected 125 coins.
Your path:
[3, 0]
[3, 4]
[3, 0]
[3, 1]
[2, 1]
[1, 1]
[1, 2]'''

'''
8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left

Game over! You've collected 0 coins.
Your path:
[5, 2]
[4, 2]
[5, 2]
[4, 2]
[4, 1]'''