def abs_val(num):
    return [abs(float(x)) for x in num]


numbers = input().split()

absol_val = abs_val(numbers)
print(absol_val)