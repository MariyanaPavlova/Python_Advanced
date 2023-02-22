m, n = (int(x) for x in input().split())

first = set()
second = set()

for i in range(m):
    first.add(int(input()))

for j in range(n):
    second.add(int(input()))

common = first.intersection(second)

print(*common, sep="\n")