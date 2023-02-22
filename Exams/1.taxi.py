from collections import deque

customer = deque((int(x) for x in input().split(", ")))
taxi = [int(x) for x in input().split(", ")]

total_time = 0

while customer and taxi:
    time_cust = customer[0]
    time_taxi = taxi[-1]

    if time_cust <= time_taxi:
        total_time += time_cust
        customer.popleft()
        taxi.pop()

    else:
        taxi.pop()

if customer:
    print(f'Not all customers were driven to their destinations\n'
          f'Customers left: {", ".join(str(x) for x in customer)}')
else:
    print(f'All customers were driven to their destinations\n'
          f'Total time: {total_time} minutes')


