def only_ever_n(txt):
    minn = min(int(x) for x in text.split())
    maxx = max(int(x) for x in text.split())
    summ = sum(int(x) for x in text.split())
    return minn, maxx, summ


text = input()
output = only_ever_n(text)
print(f'The minimum number is {output[0]}')
print(f'The maximum number is {output[1]}')
print(f'The sum number is: {output[2]}')