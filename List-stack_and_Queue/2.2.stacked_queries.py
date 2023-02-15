n = int(input())

stack = []

for i in range(n):
    query = input().split()

    if query[0] == "1":
        number = query[-1]
        stack.append(int(number))
    elif query[0] == "2":
        if stack:
            stack.pop()
    elif query[0] == "3" and stack:
        print(max(stack))
    elif query[0] == "4" and stack:
        print(min(stack))

#rev = stack[::-1]
rev = reversed(stack)

print(*rev, sep=", ")



