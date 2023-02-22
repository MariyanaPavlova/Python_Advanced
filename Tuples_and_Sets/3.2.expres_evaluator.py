from collections import deque

el = input().split()
numb = deque()

for i in el:
    if i in "+-*/":
        while len(numb) > 1:
            first = numb.popleft()
            sec = numb.popleft()

            result = 0
            if i == "+":
                result = first + sec
            elif i == "-":
                result = first - sec
            elif i == "*":
                result = first * sec
            elif i == "/":
                result = first // sec
            numb.appendleft(result)
    else:
        numb.append(int(i))

print(numb.popleft())