import sys
from io import StringIO

input1 = '''-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'''
input2 = '''2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'''

sys.stdin = StringIO(input1)
#sys.stdin = StringIO(input2)

nums = (float(x) for x in input().split())

dic = {}

for i in nums:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1


for key, value in dic.items():
    print(f'{key} - {value} times')
