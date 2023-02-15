n = int(input())
odd_sum = set()
even_sum = set()

for i in range(1, n+1):
    name_sum = sum([ord(x) for x in input()]) // i

    if name_sum % 2 == 0:
        even_sum.add(name_sum)
    else:
        odd_sum.add(name_sum)

if sum(odd_sum) == sum(even_sum):
    x = odd_sum.union(even_sum)
    print(*x, sep=", ")
elif sum(odd_sum) > sum(even_sum):
    y = odd_sum.difference(even_sum)
    print(*y, sep=", ")
elif sum(odd_sum) < sum(even_sum):
    z = odd_sum.symmetric_difference(even_sum)
    print(*z, sep=", ")


