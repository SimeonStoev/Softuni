n = int(input())
cars = {}

for _ in range(n):
    car_data = input().split("|")
    car = car_data[0]
    mileage = int(car_data[1])
    fuel = int(car_data[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]["fuel"] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            cars.pop(car)
            print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        fuel_to_recharge = 0
        if cars[car]["fuel"] + fuel > 75:
            fuel_to_recharge = 75 - cars[car]["fuel"]
        else:
            fuel_to_recharge = fuel

        cars[car]["fuel"] += fuel_to_recharge
        print(f"{car} refueled with {fuel_to_recharge} liters")
    elif command[0] == "Revert":
        car = command[1]
        distance = int(command[2])
        if cars[car]["mileage"] - distance < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= distance
            print(f"{car} mileage decreased by {distance} kilometers")

for key, value in cars.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
