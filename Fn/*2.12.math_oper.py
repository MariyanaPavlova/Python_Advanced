from collections import deque

def math_operations(*args, **kwargs):
    que = deque(args)
    while que:
        kwargs["a"] += que.popleft()
        if not que:
            break

        kwargs["s"] -= que.popleft()
        if not que:
            break

        number = que.popleft()
        if number != 0:
            kwargs["d"] /= number
        if not que:
            break

        kwargs["m"] *= que.popleft()

    return kwargs

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))