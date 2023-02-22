from collections import deque

fireworks = deque(int(x) for x in input().split(", "))
explosives = list(int(x) for x in input().split(", "))

firework_types = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while fireworks and explosives:
    el_fire = fireworks[0]
    el_expl = explosives[-1]
    sum_el = el_fire + el_expl

    if el_fire <= 0:
        fireworks.popleft()
        continue
    if el_expl <= 0:
        explosives.pop()
        continue

    if sum_el % 3 == 0 and sum_el % 5 != 0:
        firework_types["Palm Fireworks"] += 1
        fireworks.popleft()
        explosives.pop()

    elif sum_el % 5 == 0 and sum_el % 3 != 0:
        firework_types["Willow Fireworks"] += 1
        fireworks.popleft()
        explosives.pop()

    elif sum_el % 3 == 0 and sum_el % 5 == 0:
        firework_types["Crossette Fireworks"] += 1
        fireworks.popleft()
        explosives.pop()

    else:
        el_fire = el_fire -1
        fireworks.append(el_fire)
        fireworks.popleft()

perfect_f = 0

for k, v in sorted(firework_types.items(), key=lambda x: x[1]):
    if v >= 3:
        perfect_f += 1

if perfect_f >= 3:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f'Firework Effects left: {", ".join(str(x) for x in fireworks)}')
if explosives:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosives)}')

for k, v in firework_types.items():
    print(f'{k}: {v}')