green_duration = int(input())
free_window = int(input())

car = input()

green_wind = green_duration
total_car = 0
crashed = False

while not car == "END":

    if car == 'green':
        green_wind = green_duration

    elif car != 'green' and green_wind > 0:

        if len(car) <= green_wind:
            green_wind -= len(car)
            total_car += 1

        else:
            hit_character = car[green_wind + free_window]
            print(f"A crash happened!")
            print(f'{car} was hit at {hit_character}.')
            crashed = True
            break

    car = input()

if not crashed:
    print('Everyone is safe.')
    print(f'{total_car} total cars passed the crossroads.')