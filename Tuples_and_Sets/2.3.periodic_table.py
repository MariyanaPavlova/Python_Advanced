n = int(input())

elem = set()

for i in range(n):
    cur_el = input().split()
    elem = elem.union(cur_el)

print(*elem, sep="\n")
