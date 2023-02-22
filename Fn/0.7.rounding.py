def rounding(strr):
    return [round(x) for x in strr]

string = [float(x) for x in input().split(" ")]
print(rounding(string))