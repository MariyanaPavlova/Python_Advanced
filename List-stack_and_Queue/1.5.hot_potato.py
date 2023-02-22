from collections import deque

kids = deque(input().split())
n = int(input())

while kids:
    kids.rotate(-n)
    print(f'Removed {kids.pop()}')

print(f'Last is {kids.popleft()}')

# from collections import deque
#
# kids = deque(input().split())
# n = int(input())
#
# while len(kids)>1:
#     for i in range(1, n+1):
#         if i % n == 0:
#             print(f'Removed {kids.popleft()}')
#             break
#         kids.append(kids.popleft())
# print(f'Last is {" ".join(kids)}')
