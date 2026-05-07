# This script simulates a parking lot by processing a series of commands to add or remove cars.
# It uses a set to track cars currently in the lot and prints the remaining cars or a message if empty.

# Read the number of commands (car entries/exits)
number_of_cars = int(input())

# Initialize an empty set to represent the parking lot
car_lot = set()

# Loop for each command
for _ in range(number_of_cars):
    # Read the command as a list split by ", "
    command = input().split(", ")
    # Extract the direction ("IN" or "OUT")
    direction = command[0]
    # Extract the car identifier
    car = command[1]
    # If direction is "IN", add the car to the set
    if direction == "IN":
        car_lot.add(car)
    # If direction is "OUT", remove the car from the set (assuming it exists)
    elif direction == "OUT":
        car_lot.remove(car)

# Check if the parking lot is empty
if len(car_lot) == 0:
    print("Parking Lot is Empty")
else:
    # Print each car in the lot on a new line
    print('\n'.join(car_lot))
