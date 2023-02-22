from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))
milkshakes = 0

while chocolates and milk_cups:
    if chocolates[-1] == milk_cups[0] and milk_cups and chocolates:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
        if milkshakes == 5:
            break

    elif chocolates[-1] <= 0 or milk_cups[0] <= 0 and milk_cups and chocolates:
        if chocolates[-1] <= 0:
            chocolates.pop()
        else:
            milk_cups.popleft()

    elif chocolates[-1] != milk_cups[0] and milk_cups and chocolates:
        milk_cups.append(milk_cups.popleft())
        chocolates[-1] -= 5


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)}')
else:
    print("Chocolate: empty")
if milk_cups:
    print(f'Milk: {", ".join(str(x) for x in milk_cups)}')
else:
    print("Milk: empty")