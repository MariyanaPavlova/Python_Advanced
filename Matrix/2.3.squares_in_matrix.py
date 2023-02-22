row, col = (int(x) for x in input().split())

matrix = []

for i in range(row):
    matrix.append(input().split())

sum_matrix = []
sqr = 0
for i in range(row-1):
    for j in range(col-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            sqr += 1
print(sqr)


