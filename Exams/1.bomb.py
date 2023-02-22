from collections import deque

bomb_effect = deque((int(x) for x in input().split(", ")))
bomb_casing = list(int(x) for x in input().split(", "))

bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

bombs_table = {40: 'Datura Bombs',
               60: "Cherry Bombs",
               120: "Smoke Decoy Bombs"}

success = False

# def bomb_filled(bombs):
#     for i in bombs.values():
#         if i < 3:
#             return False
#     return True

while bomb_effect and bomb_casing: # можем да го направим и с функция
#while bomb_effect and bomb_casing and not bomb_filled(bombs):
    bomb_effect_el = bomb_effect[0]
    bomb_casing_el = bomb_casing[-1]

    sum = bomb_casing_el + bomb_effect_el

    if sum == 40: # може да се реши с 2 ри речник
        bombs['Datura Bombs'] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    elif sum == 60:
        bombs['Cherry Bombs'] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    elif sum == 120:
        bombs['Smoke Decoy Bombs'] += 1
        bomb_effect.popleft()
        bomb_casing.pop()

    # if sum in bombs_table:
    #     bomb_type = bombs_table[sum]
    #     bombs[bomb_type] += 1
    #
    #     bomb_effect.popleft()
    #     bomb_casing.pop()

    else:
        bomb_casing[-1] -= 5

    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        success = True
        break

if success:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effect)}')

if not bomb_casing:
    print("Bomb Casings: empty")
else:
    print(f'Bomb Casings: {", ".join(str(x) for x in bomb_casing)}')

sort_bombs = sorted(bombs.items())
for key, value in sort_bombs:
    print(f'{key}: {value}')
