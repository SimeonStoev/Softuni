number_of_cars = int(input())
car_lot = set()

for _ in range(number_of_cars):
    command = input().split(", ")
    direction = command[0]
    car = command[1]
    if direction == "IN":
        car_lot.add(car)
    elif direction == "OUT":
        car_lot.remove(car)

if len(car_lot) == 0:
    print("Parking Lot is Empty")
else:
    print('\n'.join(car_lot))
