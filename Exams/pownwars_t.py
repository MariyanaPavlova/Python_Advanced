b_coord = []
w_coord = []

b_letters_c = ""
w_letters_c = ""

for i in range(1, 9):
    data = input().split()
    if "w" in data:
        w_coord = [i, data.index('w')]
    if "b" in data:
        b_coord = [i, data.index("b")]

row_dif = abs(w_coord[0] - b_coord[0])
col_dif = abs(w_coord[1] - b_coord[1])

white = False
black = False

letters = 'abcdefgh'

for i, ind in enumerate(letters):
    if b_coord[1] == i:
        b_letters_c = ind
    if w_coord[1] == i:
        w_letters_c = ind

if abs(b_coord[0] - w_coord[0]) >=2:
    if 8 - b_coord[0] > 8 - w_coord[0]:
        print(f'Game over! White pawn is promoted to a queen at {w_letters_c}8.')
    else:
        print(f'Game over! Black pawn is promoted to a queen at {b_letters_c}8.')

else:
    pass

