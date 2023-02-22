import math

def is_in_range(row, cow):
    if row in range(7) and cow in range(7): #същото като 0 <= row < 7 and 0 <= col < 7
        return True
    return False

def is_number(el):
    try:
        return int(el)
    except Exception:
        return False

N = 7
player_1, player_2 = input().split(", ")

points = {player_1: 501, player_2: 501}
players_turn = {0: player_2, 1: player_1}

turns_count = 0
matrix = []

for _ in range(N):
    matrix.append(input().split())


while True:
    row, col = eval(input())
    turns_count += 1

    if is_in_range(row, col):
        number = is_number(matrix[row][col])
        if number:
            points[players_turn[turns_count % 2]] -= number

        curr_points = sum([   # взимаме всички ел. по 4 края на матрицата
            int(matrix[0][col]),
            int(matrix[-1][col]),
            int(matrix[row][0]),
            int(matrix[row][-1])
        ])

        if matrix[row][col] == "D":
            points[players_turn[turns_count % 2]] -= curr_points * 2

        if matrix[row][col] == "T":
            points[players_turn[turns_count % 2]] -= curr_points * 3

        if matrix[row][col] == "B":
            print(f'{players_turn[turns_count % 2]} won the game with {math.ceil(turns_count/2)} throws!')
            exit(0)

        if points[player_1] <= 0 or points[player_2] <= 0:
            break


print(f'{players_turn[turns_count % 2]} won the game with {math.ceil(turns_count/2)} throws!')


'''Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)

Ivan won the game with 1 throws!
'''

'''George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)

Hristo won the game with 4 throws!
'''