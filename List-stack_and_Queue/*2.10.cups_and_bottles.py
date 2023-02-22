from collections import deque

cups = deque((int(x) for x in input().split()))
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    last_bottle = bottles[-1]
    first_cup = cups[0]

    if last_bottle >= first_cup:
        last_bottle -= first_cup
        if last_bottle > 0:
            wasted_water += last_bottle
        cups.popleft()
        bottles.pop()
    else:
        first_cup -= last_bottle
        cups[0] = first_cup
        bottles.pop()

if not cups:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
print(f"Wasted litters of water: {wasted_water}")