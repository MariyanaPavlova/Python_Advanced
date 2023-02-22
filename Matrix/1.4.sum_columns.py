row, col = (int(x) for x in input().split(', '))

matrix = []

for i in range(row):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)


for j in range(col):
    summ = 0
    for i in range(row):
        summ += int(matrix[i][j])

    print(summ)
