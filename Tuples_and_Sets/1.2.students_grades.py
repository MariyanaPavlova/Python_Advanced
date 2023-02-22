import sys
from io import StringIO

input1 = '''7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00'''

sys.stdin = StringIO(input1)

n = int(input())
dict = {}

def average(nums):
    return sum(nums)/len(nums)

for i in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in dict:
        dict[name] = []
    dict[name].append(grade)

for name, grades in dict.items():
    averige = average(grades)
    grade_str = " ".join(str(f'{x:.2f}') for x in grades)
    print(f'{name} -> {grade_str} (avg: {averige:.2f})')