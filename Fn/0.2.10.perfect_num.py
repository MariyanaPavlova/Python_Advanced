def perfect(num):
    new = 0
    for i in range(1, num + 1):
        if num % i == 0:
            new += i

    if new / 2 == num:
        return True
    return False

n = int(input())
if perfect(n):
    print(f'We have a perfect number!')
else:
    print(f"It's not so perfect.")

****

def perfect(num):
    new = 0
    for i in range(1, num + 1):
        if num % i == 0:
            new += i

    if new / 2 == num:
        return f'We have a perfect number!'
    else:
        return "It's not so perfect."


n = int(input())
print(perfect(n))