"""
Traffic Light Intersection Simulator

This program simulates a traffic intersection with a green light and yellow light.
Cars arrive in a queue and pass through the intersection when the green light is active.
A crash occurs if a car extends beyond the yellow light time limit, hitting the traffic light.
"""

from collections import deque

# Read traffic light durations (in car length units)
green_light = int(input())  # Duration of green light per cycle
yellow_light = int(input())  # Duration of yellow light per cycle

cars = deque()  # Queue to hold incoming cars (represented as strings)

crash_happened = False  # Flag to track if a collision occurred
total_cars_passed = 0  # Counter for cars that successfully passed

# Main event loop: process commands until "END" is received
while True:
    command = input()

    if command == "END":
        break

    # Process a green light cycle
    if command == "green":
        curr_green_light = green_light  # Remaining green light time for this cycle
        curr_yellow_light = yellow_light  # Remaining yellow light time

        # Process cars in the queue during the green light
        while curr_green_light > 0 and len(cars) > 0:
            car = cars.popleft()  # Get the next car from the queue
            total_cars_passed += 1
            car_len = len(car)  # Car length (number of characters)
            curr_green_light -= car_len  # Subtract car length from available green light time

            # Check if the car extends into the yellow light period
            if curr_green_light < 0:
                # The car extends beyond the green light; it enters the yellow light zone
                curr_yellow_light = abs(curr_green_light)  # Remaining distance car extends
                curr_green_light = 0

            # Detect crash: if car extends beyond the allowed yellow light duration
            if curr_yellow_light > yellow_light:
                crash_happened = True
                print("A crash happened!")
                # Print the character in the car string that caused the collision
                print(f"{car} was hit at {car[-(curr_yellow_light - yellow_light)]}.")
                break

            # Exit if crash already happened
            if crash_happened:
                break
    else:
        # Any other command is treated as a car arriving at the intersection
        cars.append(command)

# Output results
if not crash_happened:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
