n = int(input())
lot = set()

for i in range(n):
    directions, car_numb = input().split(", ")
    if directions == "IN":
        lot.add(car_numb)
    elif directions == "OUT":
        lot.remove(car_numb)

if lot:
    print("\n".join(lot))
else:
    print('Parking Lot is Empty')