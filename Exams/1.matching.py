from collections import deque

males = list((int(x) for x in input().split()))
females = deque(int(x) for x in input().split())

matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue

    if female <= 0:
        females.popleft()
        continue

    if male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if male == female:
        males.pop()
        females.popleft()
        matches += 1

    elif male != female:
        females.popleft()
        males[-1] = males[-1] - 2


males_left = list(reversed(males))

print(f'Matches: {matches}')
if males_left:
    print(f"Males left: {', '.join(str(x) for x in males_left)}")
else:
    print(f'Males left: none')

if females:
    print(f'Females left: {", ".join(str(x) for x in females)}')
else:
    print(f'Females left: none')
