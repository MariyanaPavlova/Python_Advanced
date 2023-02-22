values = ["a", "b", "c"]
index = 0

for i in values:
    print(i, index)
    index +=1
# a 0
# b 1
# c 2

for i in range(len(values)):
    v = values[i]
    print(i, v)
# 0 a
# 1 b
# 2 c

for i, v in enumerate(values):
    print(i, v)
# 0 a
# 1 b
# 2 c