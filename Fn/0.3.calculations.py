def calculates(operator, first: int, sec: int):
    if operator == "multiply":
        return first * sec
    elif operator == 'divide':
        return first // sec
    elif operator == "add":
        return first + sec
    elif operator == "subtract":
        return first - sec


oper = input()
first = int(input())
second = int(input())
print(calculates(oper, first, second))
