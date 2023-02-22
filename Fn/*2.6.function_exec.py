def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*args):
    results = []
    for func_name, data in args: #((sum_numbers, (1, 2)) tuple of 2 el tuples
        res = func_name(*data)
        results.append(res)
    return results

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

