def character(n1, n2):
    a = []
    for i in range(ord(n1)+1, ord(n2)):
        a.append(chr(i))
    return a


n11 = input()
n22 = input()
out = character(n11, n22)
print(*out, sep=" ")