# n = int(input())
#
# matrix = []
#
# for i in range(n):
#     matrix.append(list(input()))
#
# position = None
# searched_ch = input()
#
# for i in range(n):
#     for j in range(n):
#         if searched_ch == matrix[i][j]:
#             position = (i, j)
#             print(position)
#             break
#     if position:
#         break
#
# if not position:
#     print(f'{searched_ch} does not occur in the matrix')
#
# *****
r = int(input())
matrix = [list(input()) for _ in range(r)]

element = input()
coordinates = None

for row in matrix:
    if element in row:
        coordinates = (matrix.index(row), row.index(element))
        print(coordinates)
        break

if not coordinates:
    print(f"{element} does not occur in the matrix")
