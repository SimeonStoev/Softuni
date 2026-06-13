from collections import deque

fuel = [int(i) for i in input().split()]
decrease_index = deque([int(i) for i in input().split()])
fuel_needed = deque([int(i) for i in input().split()])

altitudes = []
curr_altitude = 0
offroad_succeeded = True

while len(fuel) > 0 and len(decrease_index) > 0:
    curr_fuel = fuel[-1]
    curr_decrease_index = decrease_index[0]
    curr_fuel_needed = fuel_needed[0]
    curr_altitude += 1

    if curr_fuel - curr_decrease_index >= curr_fuel_needed:
        print(f"John has reached: Altitude {curr_altitude}")
        altitudes.append(f"Altitude {curr_altitude}")
        fuel.pop()
        decrease_index.popleft()
        fuel_needed.popleft()
    else:
        offroad_succeeded = False
        print(f"John did not reach: Altitude {curr_altitude}")
        break

if not offroad_succeeded:
    if len(altitudes) > 0:
        print("John failed to reach the top.")
        print(f"Reached altitudes: {', '.join(altitudes)}")
    else:
        print("John failed to reach the top.")
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
