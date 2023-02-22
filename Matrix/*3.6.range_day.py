def is_outside(row, col, sizee):
    if row < 0 or col < 0 or row >= sizee or col >= sizee:
        return True
    return False


def get_next_posit(direct, row, col, st):
    if direct == 'up':
        return row - st, col
    if direct == 'left':
        return row, col - st
    if direct == 'right':
        return row, col + st
    if direct == 'down':
        return row + st, col


size = 5
matrix = []

targets = 0
hit_targets = []

pl_row, pl_col = 0, 0

for i in range(size):
    data = input().split()
    matrix.append(data)
    for j in range(size):
        el = data[j]
        if el == "A":
            pl_row, pl_col = i, j
        if el == "x":
            targets +=1

n = int(input())

for _ in range(n):
    line_commands = input().split()
    command = line_commands[0]
    dir = line_commands[1]

    if command == "move":
        step = int(line_commands[-1])

        next_row, next_col = get_next_posit(dir, pl_row, pl_col, step) #взимаме нова поз. с дад стъпка (step)

        if is_outside(next_row, next_col, size):
            continue
        if matrix[next_row][next_col] != ".":
            continue

        matrix[pl_row][pl_col] = "."
        matrix[next_row][next_col] = "A"

        pl_row, pl_col = next_row, next_col  # презаписваме позицията защото функ.раб.с pl_row pl_col

    elif command == "shoot":

        shoot_row, shoot_col = get_next_posit(dir, pl_row, pl_col, 1)  # взимаме нова поз.стъпка 1

        while True:         #-въртим докато не излезем извън границите или не уцелим бомба
            if is_outside(shoot_row, shoot_col, size):
                break

            if matrix[shoot_row][shoot_col] == "x":
                hit_targets.append([shoot_row, shoot_col])
                matrix[shoot_row][shoot_col] = "."
                break

            shoot_row, shoot_col = get_next_posit(dir, shoot_row, shoot_col, 1) # презаписваме позицията

        if len(hit_targets) == targets:
            break

if len(hit_targets) == targets:
    print(f'Training completed! All {targets} targets hit.')
else:
    print(f'Training not completed! {targets-len(hit_targets)} targets left.')

for x in hit_targets:
    print(x)


'''
. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 1

Training not completed! 3 targets left.
[4, 1]
'''

'''
. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right

Training completed! All 2 targets hit.
[4, 1]
[2, 2]
'''

'''
. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left

Training not completed! 1 targets left.
[4, 1]
'''