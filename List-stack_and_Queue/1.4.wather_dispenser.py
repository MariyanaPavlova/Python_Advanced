import sys
from io import StringIO

input1 = '''2
Peter
Amy
Start
2
refill 1
1
End'''

input2 = '''10
Peter
George
Amy
Alice
Start
2
3
3
3
End'''
sys.stdin = StringIO(input1)
#sys.stdin = StringIO(input2)

from collections import deque

liters = int(input())
line = deque()
name = input()

while not name == "Start":
    line.append(name)
    name = input()

comand = input()
while not comand == 'End':
    if comand.isdigit():
        name = line.popleft()
        if liters >= int(comand):
            liters -= int(comand)
            print(f'{name} got water')
        else:
            print(f'{name} must wait')

    elif comand.startswith("refill"):
        _, refil = comand.split()
        refil = int(refil)
        liters += refil
    comand = input()
print(f'{liters} liters left')

