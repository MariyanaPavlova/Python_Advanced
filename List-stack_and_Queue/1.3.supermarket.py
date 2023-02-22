import sys
from io import StringIO

input1 = ''' George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End
'''
input2 = '''Anna
Emma
Alexander
End'''

#sys.stdin = StringIO(input1)
#sys.stdin = StringIO(input2)

from collections import deque

name = input()
line = deque()

while not name == 'End':
    if name == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(name)
    name = input()
print(f'{len(line)} people remaining.')


