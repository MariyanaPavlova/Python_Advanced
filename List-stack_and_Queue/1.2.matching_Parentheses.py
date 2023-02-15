expr = input()

stack = []

for i in range(len(expr)):
    if expr[i] == "(":
        stack.append(i)

    elif expr[i] == ")":
        start = stack.pop()
        print(expr[start:i+1])