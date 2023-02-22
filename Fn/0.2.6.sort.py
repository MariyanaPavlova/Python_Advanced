def only_ever_n(txt):
    out = sorted(int(x) for x in text.split())
    return out


text = input()
output = only_ever_n(text)
print(output)