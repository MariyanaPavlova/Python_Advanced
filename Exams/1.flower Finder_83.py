from collections import deque

vowels = deque(input().split())
conson = list(input().split())
dict = {"rose": 4, "tulip": 5, "lotus": 5, "daffodil": 8}

final = ""
ex = False

while vowels and conson and not ex:
    v = vowels.popleft()
    c = conson.pop()

    for key in dict:
        if v in key:
            count = key.count(v)
            dict[key] -= count
            if dict[key] <= 0:
                final = key
                print(f"Word found: {final}")
                ex = True
                break

        if c in key:
            count = key.count(c)
            dict[key] -= count
            if dict[key] <= 0:
                final = key
                print(f"Word found: {final}")
                ex = True
                break

if not final:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if conson:
    print(f"Consonants left: {' '.join(str(x) for x in conson)}")

