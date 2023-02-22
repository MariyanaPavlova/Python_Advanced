def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def get_next_posit(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def get_houses_in_range(size, r, c): # връща списък с валидни коорд.до дядо коледа
    houses = []
    if not is_outside(r - 1, c, size):
        houses.append([r - 1, c])
    if not is_outside(r + 1, c, size):
        houses.append([r + 1, c])
    if not is_outside(r, c + 1, size):
        houses.append([r, c + 1])
    if not is_outside(r, c - 1, size):
        houses.append([r, c - 1])
    return houses


presents = int(input())
size = int(input())

matrix = []

santa_row, santa_col = 0, 0
initial_good_kids_count = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        el = data[col]
        if el == "S":
            santa_row, santa_col = row, col
        elif el == "V":
            initial_good_kids_count += 1

good_kids_count = initial_good_kids_count

while True:
    command = input()
    if command == "Christmas morning":
        break

    next_santa_row, next_santa_col = get_next_posit(command, santa_row, santa_col) #викаме функц.1

    if matrix[next_santa_row][next_santa_col] == "V":
        good_kids_count -= 1
        presents -= 1

    elif matrix[next_santa_row][next_santa_col] == "C":
        houses_in_range = get_houses_in_range(size, next_santa_row, next_santa_col) #взимаме коорд от функ.

        for row, col in houses_in_range:
            if matrix[row][col] == "X":
                presents -= 1
            if matrix[row][col] == "V":
                presents -= 1
                good_kids_count -=1
            matrix[row][col] = "-"
            if presents == 0:
                break

    matrix[santa_row][santa_col] = "-"
    matrix[next_santa_row][next_santa_col] = "S"
    santa_row, santa_col = next_santa_row, next_santa_col # презаписваме коорд.2

    if presents == 0:
        break

if presents == 0 and good_kids_count > 0:
    print('Santa ran out of presents!')

for row_el in matrix:
    print(" ".join(row_el))

if good_kids_count == 0:
    print(f'Good job, Santa! {initial_good_kids_count} happy nice kid/s.')
else:
    print(f'No presents for {good_kids_count} nice kid/s.')