import re

def is_inside(size, row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def count_all_bombs(ma, ro, co):
    count = 0
    if is_inside(len(matrix), ro - 1, co) and matrix[ro - 1][co] == '*': #up
        count += 1
    if is_inside(len(matrix), ro + 1, co) and matrix[r + 1][co] == '*': #down
        count += 1
    if is_inside(len(matrix), ro, co + 1) and matrix[ro][co + 1] == '*': #right
        count += 1
    if is_inside(len(matrix), ro, co - 1) and matrix[ro][co - 1] == '*': #left
        count += 1
    if is_inside(len(matrix), ro - 1, co + 1) and matrix[ro - 1][co + 1] == '*': #up-right
        count += 1
    if is_inside(len(matrix), ro - 1, co - 1) and matrix[ro - 1][co - 1] == '*': #up-left
        count += 1
    if is_inside(len(matrix), ro + 1, co - 1) and matrix[ro + 1][co - 1] == '*': #down-left
        count += 1
    if is_inside(len(matrix), ro + 1, co + 1) and matrix[ro + 1][co + 1] == '*': #down-right
        count += 1
    return count

n = int(input())

matrix = []

for _ in range(n):
    matrix.append([0] * n)

bomb_count = int(input())

for _ in range(bomb_count):
    row, col = re.findall('\d+', input())
    row = int(row)
    col = int(col)
    matrix[row][col] = "*"

for r in range(n):
    for c in range(n):
        if matrix[r][c] == "*":
            pass
        else:
            cell_value = count_all_bombs(matrix, r, c)
            matrix[r][c] = cell_value

for x in matrix:
    print(*x, sep=" ")


'''
4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)


1 1 2 *
1 * 3 2
2 3 * 1
* 2 1 1

'''

'''
5
3
(1, 1)
(2, 4)
(4, 1)


1 1 1 0 0
1 * 1 1 1
1 1 1 1 *
1 1 1 1 1
1 * 1 0 0
'''