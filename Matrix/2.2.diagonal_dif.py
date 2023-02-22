n = int(input())

matrix = []

for i in range(n):
    num = [int(x) for x in input().split()]
    matrix.append(num)

prim_diagonal = []
sec_diagonal = []

for i in range(n):
    prim_diagonal.append(matrix[i][i])
    sec_diagonal.append(matrix[i][n-1-i])

summ = sum(prim_diagonal)-sum(sec_diagonal)
print(abs(summ))