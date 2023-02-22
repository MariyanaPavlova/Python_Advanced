def filter_even(iters):
    return list(filter(lambda x: x%2 == 0, iters))

num = map(int, input().split())     #1 2 3 4
print(filter_even(num))
