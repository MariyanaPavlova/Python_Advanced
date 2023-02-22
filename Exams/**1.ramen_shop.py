from collections import deque

bowls = list((int(x) for x in input().split(", ")))
customers = deque(int(x) for x in input().split(", "))


while bowls and customers:
    bowl = bowls[-1]
    cust = customers[0]

    if bowl == cust:
        bowls.pop()
        customers.popleft()

    if bowl > cust:
        bowls[-1] -= cust
        customers.popleft()
        continue

    if cust > bowl:
        customers[0] -= bowl
        bowls.pop()
        continue


if not customers:
    print(f'Great job! You served all the customers.')
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")