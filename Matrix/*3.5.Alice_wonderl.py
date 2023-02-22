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
possit = []

for i in range(n):
    data = input().split()
    matrix.append(data)
    if "A" in data:
        possit = [i, data.index("A")]

command = input()
a_row, a_col = possit

no_party = False
party = True
tea_bags = 0


while command:

    matrix[a_row][a_col] = "*"
    next_row, next_col = get_next_posit(command, a_row, a_col)

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        no_party = True
        break

    if matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        no_party = True
        break

    if matrix[next_row][next_col] != "." and matrix[next_row][next_col] != "*":
        tea_bags += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '*'

    a_row, a_col = next_row, next_col
    matrix[next_row][next_col] = '*'

    if tea_bags == 10:
        break

    command = input()

if no_party:
    print(f"Alice didn't make it to the tea party.")
if tea_bags >= 10:
    print(f"She did it! She went to the party.")

for x in matrix:
    print(*x, sep=" ")

'''
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left


Alice didn't make it to the tea party.
. * . . 1
* * * . .
4 * . 1 .
. . . 2 .
. 3 . . .
'''

'''
7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right


She did it! She went to the party.
* * . 1 1 . .
* . . . 6 . 5
* * . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2

'''