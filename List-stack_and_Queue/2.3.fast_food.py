from collections import deque

quantity = int(input())

sequency = deque(int(x) for x in input().split())

print(max(list(sequency)))

while sequency:

    order = sequency[0]
    if quantity - order >= 0:
        quantity -= order
        sequency.popleft()
    else:
        break

if sequency:
    print(f'Orders left: {" ".join(str(x) for x in sequency)}')
else:
    print(f'Orders complete')