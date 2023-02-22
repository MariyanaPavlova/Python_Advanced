n = int(input())

matrix = []

for i in range(n):
    num = [int(x) for x in input().split()]
    matrix.append(num)

diagonal = 0

for i in range(n):
    diagonal += matrix[i][i]

print(diagonal)