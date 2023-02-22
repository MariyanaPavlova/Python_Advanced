def points_gain(matr, col):
    points = 0
    for i in range(6):
        if matrix[i][col] != "B":
            points += int(matrix[i][col])
    return points

matrix = []

for i in range(6):
    matrix.append(input().split())

pointss = 0
#points = 0
for _ in range(3):
    row, col = input().strip('()').split(', ')
    row = int(row)
    col = int(col)

    #if 0 <= row < 6 and 0 <= col < 6: - може с try except
    try:
        if matrix[row][col] == 'B':
            matrix[row][col] = "0"
            pointss += points_gain(matrix, col)
        # for i in range(6): - може с функцията горе
        #     if matrix[i][col] != "B":
        #         points += int(matrix[i][col])
    except IndexError:
        continue

prize = ""

if pointss < 100:
    print(f"Sorry! You need {100-pointss} points more to win a prize.")
else:
    if 100 <= pointss <= 199:
        prize = "Football"
    elif 200 <= pointss <= 299:
        prize = 'Teddy Bear'
    elif pointss >= 300:
        prize = "Lego Construction Set"

    print(f"Good job! You scored {pointss} points, and you've won {prize}.")


'''
10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)

Sorry! You need 33 points more to win a prize.
'''

'''
B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)

Good job! You scored 299 points, and you've won Teddy Bear.
'''