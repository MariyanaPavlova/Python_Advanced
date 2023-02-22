n = int(input())

matrix = []
player_position = None
steps =[]
for row in range(n):
    row_data = input().split()
    matrix.append(row_data)
    if "P" in row_data:
        player_position = ([row, row_data.index("P")])
        steps.append(player_position)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
coins =0
dir = input()

while len(dir) !=0:

    if dir in directions:
        next_row = player_position[0] + directions[dir][0]
        next_col = player_position[1] + directions[dir][1]

        if next_row < 0 or next_col < 0:
            if next_col < 0:
                next_col_in = next_col + n
                steps.append([next_row, next_col_in])
            if next_row < 0:
                next_row_in = next_row + n
                steps.append([next_row_in, next_col])
        else:
            steps.append([next_row, next_col])

        if not matrix[next_row][next_col] == "X" and matrix[next_row][next_col] != "P":
            coins += int(matrix[next_row][next_col])

            matrix[next_row][next_col] = 0

        if matrix[next_row][next_col] == "X":
            coins //= 2
            print(f"Game over! You've collected {coins} coins.")
            break
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break

        player_position = [next_row, next_col]

    dir = input()

print(f'Your path:')
[print(x) for x in steps]

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