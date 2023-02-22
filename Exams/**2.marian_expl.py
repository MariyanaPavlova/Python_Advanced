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


matrix = []
rover_pos = []


for row_i in range(6):
    row_data = input().split()
    if 'E' in row_data:
        rover_pos = [row_i, row_data.index("E")]
    matrix.append(row_data)


deposit_W = 0
deposit_M = 0
deposit_C = 0

commands = input().split(", ")

for command in commands:

    curr_row, curr_col = rover_pos
    matrix[curr_row][curr_col] = "0"

    if command == 'up':
        row, col = calc_position(matrix, curr_row-1, curr_col)
    elif command == 'down':
        row, col = calc_position(matrix, curr_row+1, curr_col)
    elif command == 'right':
        row, col = calc_position(matrix, curr_row, curr_col+1)
    elif command == 'left':
        row, col = calc_position(matrix, curr_row, curr_col-1)

    coord1, coord2 = row, col
    
    if matrix[row][col] == "W":
        deposit_W += 1
        matrix[row][col] = "0"
        print(f'Water deposit found at ({coord1}, {coord2})')

    elif matrix[row][col] == "M":
        deposit_M += 1
        matrix[row][col] = "0"
        print(f'Metal deposit found at ({coord1}, {coord2})')

    elif matrix[row][col] == "C":
        deposit_C += 1
        matrix[row][col] = "0"
        print(f'Concrete deposit found at ({coord1}, {coord2})')

    elif matrix[row][col] == "R":
        print(f'Rover got broken at ({coord1}, {coord2})')
        break

    rover_pos = [row, col]


if deposit_W and deposit_M and deposit_C:
    print(f'Area suitable to start the colony.')

else:
    print(f'Area not suitable to start the colony.')

'''
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left

Water deposit found at (3, 1)
Concrete deposit found at (4, 3)
Metal deposit found at (5, 0)
Area suitable to start the colony.
'''

'''
R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right

Water deposit found at (3, 2)
Water deposit found at (4, 3)
Rover got broken at (4, 5)
Area not suitable to start the colony.
'''

'''
R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left

Water deposit found at (4, 3)
Metal deposit found at (3, 2)
Concrete deposit found at (3, 0)
Metal deposit found at (3, 5)
Rover got broken at (3, 4)
Area suitable to start the colony.
'''