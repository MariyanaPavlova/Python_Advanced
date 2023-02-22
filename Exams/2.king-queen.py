def read_board():
    return [
        [".",".",".",".",".",".",".","."],
        ["Q",".",".",".",".",".",".","."],
        [".","K",".",".",".","Q",".","."],
        [".",".",".","Q",".",".",".","."],
        ["Q",".",".",".","Q",".",".","."],
        [".","Q",".",".",".",".",".","."],
        [".",".",".",".",".",".","Q","."],
        [".","Q",".","Q",".",".",".","."],
    ]

def find_king_position(board):
    for row_ind in range(len(board)):
        # for col_ind in range(len(board[0])):
        #     if board[row_ind][col_ind] == "K":
        #         return (row_ind, col_ind)
        if "K" in board[row_ind]:
            col_ind = board[row_ind].index("K")
            return (row_ind, col_ind)

# def get_capturing_queens(board, king):
#
#     (king_row_ind, king_col_ind) = king
#     queens = []
#     # right
#     for col_ind in range(king_col_ind + 1, len(board[0]):
#         if board[king_row_ind][col_ind] == "Q":
#             queens.append((king_row_ind, col_ind))
#             break
#     # left
#     for col_ind in range(king_col_ind - 1, -1, -1):
#         if board[king_row_ind][col_ind] == "Q":
#             queens.append((king_row_ind, col_ind))
#             break
##     return queens

def in_range(value, max_value):
    return 0 <= value < max_value

def searched_with_deltas(board, king, deltas):
    rows_count = len(board)
    cols_count = len(board[0])
    (delta_row, delta_col) = deltas
    (row_ind, col_ind) = king

    while True:
        if not in_range(row_ind, rows_count) or not in_range(col_ind, cols_count):
            return None

        if board[row_ind][col_ind] == "Q":
            return (row_ind, col_ind)

        row_ind += delta_row
        col_ind += delta_col

def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]
    queens = [
        searched_with_deltas(board, king, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen]

def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print('The king is safe!')

board  = read_board()
king = find_king_position(board)
print(king)
queens = get_capturing_queens(board, king)
print_result(queens)

'''
. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .


[2, 5]
[5, 1]
[1, 0]
'''

'''
. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .


The king is safe!
'''