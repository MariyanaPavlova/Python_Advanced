from math import log

num = int(input())
base = input()

def calc_log(x, base):
    if base == "natural":
        return log(x)
    else:
        return log(x,int(base))

print(calc_log(num, base))