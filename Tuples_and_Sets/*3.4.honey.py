from collections import deque

working_bees = deque(int(x) for x in input().split())
all_nectar = [int(x) for x in input().split()]
symbol = deque(input().split())

total_honey = 0

while working_bees and all_nectar:
    bee = working_bees[0]
    nectar = all_nectar[-1]

    if bee <= nectar:
        symb = symbol.popleft()
        all_nectar.pop()
        working_bees.popleft()

        if symb == "+":
            total_honey += abs(bee + nectar)
        elif symb == "-":
            total_honey += abs(bee - nectar)
        elif symb == "*":
            total_honey += abs(bee * nectar)
        elif symb == "/" and nectar != 0:
            total_honey += abs(bee / nectar)

    else:
        if all_nectar:
            all_nectar.pop()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')
if all_nectar:
    print(f'Nectar left: {", ".join(str(x) for x in all_nectar)}')
 