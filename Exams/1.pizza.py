from collections import deque

pizzas = deque((int(x) for x in input().split(", ")))
empl_capacity = [int(x) for x in input().split(", ")]

comp_orders = 0

while pizzas and empl_capacity:
    pizza = pizzas[0]
    empl = empl_capacity[-1]


    if pizza <= 0 or pizza > 10:
       pizzas.popleft()

    elif pizza <= empl and pizza > 0:
        comp_orders += pizza
        pizzas.popleft()
        empl_capacity.pop()

    elif pizza > empl and pizza <= 10:
        comp_orders += pizzas[0]-(pizza-empl)
        pizzas[0] = pizza - empl
        empl_capacity.pop()

if not pizzas:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {comp_orders}')

if empl_capacity:
    print(f'Employees: {", ".join(str(x) for x in empl_capacity)}')

elif not empl_capacity and pizzas:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizzas)}')
