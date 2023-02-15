n = int(input())

guests = set()

for i in range(n):
    res_code = input()
    guests.add(res_code)

guest_code = input()

while not guest_code == "END":
    guests.discard(guest_code)
    guest_code = input()

print(len(guests))
guests_sort = sorted(guests)
print("\n".join(guests_sort))