expression = input()

parenth = []

balanced = True
for i in expression:
    if i in "({[":
        parenth.append(i)
    else:
        if parenth:
            last_parenth = parenth.pop()
            if f'{last_parenth}{i}' not in "()[]{}":
                balanced = False
                break
        else:
            balanced = False
if balanced:
    print('YES')
else:
    print('NO')