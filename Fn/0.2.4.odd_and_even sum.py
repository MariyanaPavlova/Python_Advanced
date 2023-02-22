def odd_even_sum(txt):
    even = 0
    odd = 0
    for i in txt:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    return odd, even


text = input()
output = odd_even_sum(text)
print(f'Odd sum = {output[0]}, Even sum = {output[1]}')
