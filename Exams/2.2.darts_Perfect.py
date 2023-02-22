from collections import deque

def create_board():
    m = []
    for x in range(7):
        m.append([x for x in input().split()])
    return m

def is_valid(ro, co):
    if 0 <= ro < 7 and 0 <= co < 7:
        return True
    return False

def triple_score(ro):
    points = int(board[ro][0]) + int(board[ro][-1]) + int(board[0][ro]) + int(board[-1][ro])
    return points * 3

def double_score(ro):
    points = int(board[ro][0]) + int(board[ro][-1]) + int(board[0][ro]) + int(board[-1][ro])
    return points * 2


players = deque(input().split(", "))
scores = deque([501, 501])

board = create_board() #дефинираме входната матр.
turns = deque([0, 0])

while True:
    darts = tuple(input().split(", "))
    r = int(darts[0][-1])
    c = int(darts[1][0])
    element = None

    player = players.popleft()
    score = scores.popleft()
    turn = turns.popleft()
    turn += 1

    if is_valid(r, c):
        element = board[r][c]
    if element:
        if element == "D":
            score -= double_score(r)
        elif element == "T":
            score -= triple_score(r)
        elif element == "B":
            break
        else:
            score -= int(element)
    if score <= 0:
        break
    players.append(player)
    scores.append(score)
    turns.append(turn)

print(f'{player} won the game with {turn} throws!')

'''
Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)

Ivan won the game with 1 throws!
'''

'''
George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)

Hristo won the game with 4 throws!
'''
