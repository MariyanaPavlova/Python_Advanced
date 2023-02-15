from collections import deque

boxes = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

toys = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}

while boxes and magic_level:
    if boxes[-1] == 0:
        boxes.pop()
    if magic_level[0] == 0:
        magic_level.popleft()

    if boxes and magic_level:
        if boxes[-1] or magic_level[0] != 0:
            material = boxes.pop()
            magic = magic_level.popleft()
            present = material * magic

            if present == 150:
                toys['Doll'] += 1
            elif present == 250:
                toys['Wooden train'] += 1
            elif present == 300:
                toys['Teddy bear'] += 1
            elif present == 400:
                toys['Bicycle'] += 1
            elif present > 0:
                material += 15
                boxes.append(material)
            elif present < 0:
                boxes.append(material + magic)

if toys['Doll'] > 0 and toys['Wooden train'] > 0 or toys['Teddy bear'] > 0 and toys['Bicycle'] > 0:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if boxes:
    print(f'Materials left: {", ".join([str(x) for x in reversed(boxes)])}')
if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

#sort_toys = sorted(toys.items(), key=lambda x: x[0]) същото като долното
sort_toys = sorted(toys.items())  # речника се сортира дефолтно по ключ

for key, value in sort_toys:
    if value > 0:
        print(f'{key}: {value}')

