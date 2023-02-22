from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()

    for i in words.keys():
        words[i] = words[i].replace(v, '')
        words[i] = words[i].replace(c, '')
        if words[i] == '':
            print(f"Word found: {i}")
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

