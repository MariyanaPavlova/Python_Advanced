first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for i in range(n):
    comand_1, comand_2, *comand_3 = input().split()
    comand_3l = [int(x) for x in comand_3]

    if comand_1 == "Add" and comand_2 == "First":
        first.update(comand_3l)
    elif comand_1 == "Add" and comand_2 == "Second":
        second.update(comand_3l)

    elif comand_1 == "Remove" and comand_2 == "First":
        for i in comand_3l:
            first.discard(i)
    elif comand_1 == "Remove" and comand_2 == "Second":
        for j in comand_3l:
            second.discard(j)

    elif comand_1 + " " + comand_2 == "Check Subset":
        print(first.issubset(second) or second.issubset(first))

first_s = sorted(first)
second_s = sorted(second)
print(*first_s, sep=", ")
print(*second_s, sep=", ")