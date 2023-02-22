from collections import deque

n = int(input())
pumps = deque()

for i in range(n):
    pumps_data = [int(x) for x in input().split()]
    pumps.append(pumps_data)

for atempt in range(n):
    tank = 0

    failed = False
    for fuel, dist in pumps:
        tank += fuel

        if dist > tank:
            failed = True
            break
        else:
            tank -= dist

    if failed:
        pumps.append(pumps.popleft())
        #pumps.rotate(-1)

    else:
        print(atempt)
        break



