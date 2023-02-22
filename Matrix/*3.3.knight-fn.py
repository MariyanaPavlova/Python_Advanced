def is_knight_placed(board, row, col):
    board_size = len(board)  # 8 по условие
    if row <= 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == "K"


def count_affected_knights(board, row, col):  # 8те поз.на коня
    resul = 0
    if is_knight_placed(board, row -2, col-1):
        resul +=1
    if is_knight_placed(board, row -2, col+1):
        resul +=1
    if is_knight_placed(board, row +2, col-1):
        resul +=1
    if is_knight_placed(board, row +2, col+1):
        resul +=1
    if is_knight_placed(board, row -1, col-2):
        resul +=1
    if is_knight_placed(board, row -1, col+2):
        resul +=1
    if is_knight_placed(board, row +1, col-2):
        resul +=1
    if is_knight_placed(board, row +1, col+2):
        resul +=1
    return resul

size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0

    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "0":
                continue

            else:
                count = count_affected_knights(matrix, r, c) #добява с колко коня се засича

            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)

'''
5 
0K0K0
K000K
00K00
K000K
0K0K0

1
'''

'''
2
KK
KK

0
'''

'''
8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK

12
'''