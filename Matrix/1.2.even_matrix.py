n = int(input())

matrix = []

for i in range(n):
    num = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(num)

print(matrix)

*****
def str_to_int(strs):
    return [int(x) for x in strs]


def read_matrix():
    row_counts = int(input())
    return [str_to_int(input().split(', ')) for _ in range(row_counts)]


def is_even(x):
    return x % 2 == 0


def get_even(values):
    return [x for x in values if is_even(x)]


def get_even_matrix(matrix):
    return [get_even(row) for row in matrix]


def print_result(matrix):
    print(matrix)


matrix = read_matrix()
even_matrix = get_even_matrix(matrix)
print_result(even_matrix)