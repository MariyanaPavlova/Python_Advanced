from collections import deque

materials = list(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

gifts_pair = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    product = material + magic

    if product < 100:
        if product %2 ==0:
            product = material *2 + magic * 3
        else:
            product = product *2
    if product > 499:
        product = product / 2

    if 100 <= product <= 199:
        gifts_pair['Gemstone'] += 1
    if 200 <= product <= 299:
        gifts_pair['Porcelain Sculpture'] += 1
    if 300 <= product <= 399:
        gifts_pair['Gold'] += 1
    if 400 <= product <= 499:
        gifts_pair['Diamond Jewellery'] += 1
    if product > 499:
        product = product / 2


if gifts_pair['Gemstone'] > 0 and gifts_pair['Porcelain Sculpture'] > 0 or gifts_pair['Gold'] >0 and gifts_pair['Diamond Jewellery'] > 0:
    print('The wedding presents are made!')
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for k, v in sorted(gifts_pair.items()):
        if v > 0:
            print(f'{k}: {v}')
