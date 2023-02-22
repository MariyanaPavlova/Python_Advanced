from collections import deque

bulet_price = int(input())
gun_size = int(input())

bulets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())

intelligence_value = int(input())
i = 0
bullets_count = 0

while locks and bulets:
    bul = bulets.pop()
    loc = locks[0]
    bullets_count += 1

    if bul <= loc:
        if locks:
            locks.popleft()
            print('Bang!')
    else:
        print('Ping!')
    i += 1
    if i % gun_size == 0 and bulets:
        print('Reloading!')

earned = intelligence_value - bullets_count * bulet_price
locks_left = len(locks)

if not locks_left:
    print(f'{len(bulets)} bullets left. Earned ${earned}')
else:
    print(f"Couldn't get through. Locks left: {locks_left}")



