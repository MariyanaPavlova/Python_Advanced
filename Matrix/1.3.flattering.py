n = int(input())
list = []

for i in range(n):
    inp = [int(x) for x in input().split(", ")]
    list.extend(inp)

print(list)


****
fin = []

for i in range(n):
    num = [int(x) for x in input().split(", ")]
    list.append(num)

for row in range(len(list)):
    for col in range(len(list[row])):
        fin.append(list[row][col])
