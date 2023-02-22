def get_next_posit(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col

presents = int(input())
size = int(input())

matrix = []
possit = []

nice = 0

santa_row, santa_col = 0, 0

for i in range(size):
    data = list(input().split())
    matrix.append(data)
    for j in range(size):
        el = data[j]
        if el == "S":
            santa_row, santa_col = i, j
        if el == "V":
            nice += 1


while True:
    command = input()
    if command == "Christmas morning":
        break

    matrix[santa_row][santa_col] = "-"
    next_row, next_col = get_next_posit(command, santa_row, santa_col)

    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        continue

    if matrix[next_row][next_col] == 'X':
        matrix[next_row][next_col] = '-'

    elif matrix[next_row][next_col] == 'V':
        matrix[next_row][next_col] = '-'
        presents -= 1
        if presents == 0:
            print(f'"Santa ran out of presents!"')

    elif matrix[next_row][next_col] == 'C': #50т джъдж
        matrix[next_row][next_col] = 'S'
        if matrix[next_row+1][next_col] != '-' and 0 <= next_row+1 <= size and 0 < next_col < size:
            matrix[next_row + 1][next_col] = "-"
            presents -= 1
            if presents == 0:
                print(f'Santa ran out of presents!')
                break

        if matrix[next_row-1][next_col] != '-' and 0 <= next_row-1 <= size and 0 <= next_col < size:
            matrix[next_row-1][next_col] = "-"
            presents -= 1
            if presents == 0:
                print(f'Santa ran out of presents!')
                break

        if matrix[next_row][next_col+1] != '-' and 0 <= next_row <= size and 0 <= next_col+1 < size:
            matrix[next_row][next_col+1] = "-"
            presents -= 1
            if presents == 0:
                print(f'Santa ran out of presents!')
                break

        if matrix[next_row][next_col-1] != '-' and 0 <= next_row <= size and 0 <= next_col-1 < size:
            matrix[next_row][next_col-1] = "-"
            presents -= 1
            if presents == 0:
                print(f'Santa ran out of presents!')
                break

    santa_row, santa_col = next_row, next_col
    matrix[santa_row][santa_col] = 'S'


good_kids_not_pres = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "V":
            good_kids_not_pres += 1

for x in matrix:
    print(*x, sep=" ")

if good_kids_not_pres:
    print(f'No presents for {good_kids_not_pres} nice kid/s.')
else:
    print(f'Good job, Santa! {nice} happy nice kid/s.')