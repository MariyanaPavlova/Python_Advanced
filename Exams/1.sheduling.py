jobs = list(int(x) for x in input().split(","))

ind = int(input())
found = jobs[ind]

sum = 0

for ind, v in enumerate(jobs):
    if v <= found:
        if ind <= ind:
            sum +=v
print(sum)

****

from collections import deque
tasks = [int(x) for x in input().split(",")]

searched_ind = int(input())
result = 0
cycles = deque(sorted([(number, index) for index, number in enumerate(tasks)]))

while cycles:
    number, index = cycles.popleft()
    result += number
    if index == searched_ind:
        print(result)
        break