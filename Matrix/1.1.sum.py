row, col = [int(x) for x in input().split(", ")]
matrix = []
summ = 0

for row in range(row):
    listt = [int(x) for x in input().split(', ')]
    matrix.append(listt)
    # summ += sum(listt) #- може и така

for row_i in range(len(matrix)):
    for col_j in range(len(matrix[row_i])):
        summ += matrix[row_i][col_j]

print(summ)
print(matrix)