n = int(input())
matrix = []

for _ in range(n):  # вх.матрица
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for i in bombs: #
    bomb_row, bomb_col = [int(x) for x in i.split(",")]
    bomb_power = matrix[bomb_row][bomb_col]

    if matrix[bomb_row][bomb_col] <= 0:
        continue

    for i in range(bomb_row - 1, bomb_row + 2):  #обикаляме около нашата дадена с коорд.бомба
        for j in range(bomb_col - 1, bomb_col + 2):
            if 0 <= i < n and 0 <= j < n and matrix[i][j] > 0:
                matrix[i][j] -= bomb_power

alive_cells = 0
alive_sum = 0

for row in matrix: #принтираме всички живи ел.
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_sum += el
print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_sum}')

for row in matrix:
    print(*row, sep=" ")
