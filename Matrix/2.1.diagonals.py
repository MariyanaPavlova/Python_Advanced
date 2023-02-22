n = int(input())

matrix = []

for i in range(n):
    num = [int(x) for x in input().split(", ")]
    matrix.append(num)

prim_diagonal = []
sec_diagonal = []

for i in range(n):
    prim_diagonal.append(matrix[i][i])
    sec_diagonal.append(matrix[i][n-1-i])

print(f'Primary diagonal: {", ".join(str(x) for x in prim_diagonal)}. Sum: {sum(prim_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in sec_diagonal)}. Sum: {sum(sec_diagonal)}')
