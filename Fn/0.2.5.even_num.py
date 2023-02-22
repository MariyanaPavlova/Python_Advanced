def only_ever_n(txt):
    out = [int(x) for x in text.split() if int(x) % 2 == 0]
    return out


text = input()
output = only_ever_n(text)
print(output)