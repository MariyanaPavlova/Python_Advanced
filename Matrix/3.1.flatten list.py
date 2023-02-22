string = input().split("|")

for row in reversed(string):
    el = row.split()
    if el:
        print(*el, sep=" ", end=" ")