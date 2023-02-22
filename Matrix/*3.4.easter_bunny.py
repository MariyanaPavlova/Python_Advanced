size = int(input())
matrix = []

bunny_row, bunny_col = 0, 0  #коорд.на В

for row in range(size):  # вход на матр.
    elements = [x for x in input().split()]
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "B":
            bunny_row, bunny_col = row, col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

def is_inside(size, r, c):
    return 0 <= r < size and 0 <= c < size

max_eggs = float('-inf')
best_direction = ''
best_path = []

for direction, step in directions.items():
    eggs = 0

    current_row, current_col = bunny_row, bunny_col
    path = []

    while True:
        current_row, current_col = step(current_row, current_col) #връща сл. стъпка

        if not is_inside(size, current_row, current_col):
            break
        if matrix[current_row][current_col] == "X":
            break

        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])

        if eggs > max_eggs:
            max_eggs, best_direction, best_path = eggs, direction, path

print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)

'''
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0

right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87
'''

'''
8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22

down
[6, 2]
[7, 2]
113
'''

#
# ****
# size = int(input())
# matrix = []
#
# for _ in range(size):
#     matrix.append(list(input().split()))
#
# coord = 0
# for row in matrix:
#     if "B" in row:
#         coordinates = (matrix.index(row), row.index("B"))
#         coord = coordinates
#
# r, c = coord[0], coord[1]
#
# ri = 0
# ri_l = []
# le = 0
# le_l = []
# up = 0
# up_l = []
# d = 0
# d_l = []
#
# for i in range(c+1,size):
#      if matrix[r][i] != "X":
#          ri += int(matrix[r][i])
#          ri_l.append([r,i])
#      else:
#          break
#
# for i in range(0, c):
#     if matrix[r][i] != "X":
#         le +=int(matrix[r][i])
#         le_l.append([r, i])
#     else:
#         break
#
# for i in range(r-1, 0,-1):
#      if matrix[i][c] != "X":
#          up += int(matrix[i][c])
#          up_l.append([i, c])
#      else:
#         break
#
# for i in range(r+1,size):
#      if matrix[i][c] != "X":
#          d += int(matrix[i][c])
#          d_l.append([i, c])
#      else:
#          break
#
# if ri > le and ri > up and ri > d:
#     print('right')
#     print("\n".join(str(x) for x in ri_l))
#     print(ri)
#
# elif d > le and d > up and d > ri:
#     print('down')
#     print("\n".join(str(x) for x in d_l))
#     print(d)
#
# elif le > ri and le > up and le > d:
#     print('left')
#     print("\n".join(str(x) for x in le_l))
#     print(le)
#
# elif up > ri and up > le and up > d:
#     print('up')
#     print("\n".join(str(x) for x in up_l))
#     print(up)
