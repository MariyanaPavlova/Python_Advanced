rows, cols = (int(x) for x in input().split())

for row in range(rows):
    for col in range(cols):
        print(f'{chr(97+row)}{chr(97+row+col)}{chr(97+row)}', end=' ')
    print()


rows, cols = map(int, input().split(' '))
matrix = [[(chr(97+i)+chr(97+i+x)+chr(97+i)) for x in range(cols)] for i in range(rows)]
print('\n'.join(' '.join (map(str, el)) for el in matrix))