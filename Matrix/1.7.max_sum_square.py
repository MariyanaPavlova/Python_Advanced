row, col = [int(x) for x in input().split(", ")]

matrix = []

for i in range(row):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = -99999999999999999999
max_sum_matrix = []

for i in range(row -1):
    for j in range(col -1):
        sub_matrix = [matrix[i][j], matrix[i][j+1],
                      matrix[i+1][j], matrix[i+1][j+1]]

        cur_sum = sum(sub_matrix)
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_sum_matrix = sub_matrix.copy()

print(max_sum_matrix[0], max_sum_matrix[1],)
print(max_sum_matrix[2], max_sum_matrix[3],)
print(max_sum)