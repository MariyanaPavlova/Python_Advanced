def factorial(n1):
    fact = 1
    for i in range(1, n1+1):
        fact *= i
    return fact


def fact_div(f1, f2):
    return f1 / f2


num1 = int(input())
num2 = int(input())
f1 = factorial(num1)
f2 = factorial(num2)
result = fact_div(f1, f2)

print(f'{result:.2f}')
