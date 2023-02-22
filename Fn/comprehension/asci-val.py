char = ['a', 'b', 'c', 'a']

result = {}

for ch in char:
    result[ch] = ord(ch)
print(result)


result = {ch: ord(ch) for ch in char}
print(result)