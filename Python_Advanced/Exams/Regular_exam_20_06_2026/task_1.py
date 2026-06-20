from collections import deque

drones = {
    "Sentinel-X": 100,
    "Viper-MKII": 85,
    "Aegis-7": 75,
    "Striker-R": 65,
    "Titan-Core": 55
}

built_drones = []

mechanical_parts = [int(i) for i in input().split()]
energy_levels = deque([int(i) for i in input().split()])

while len(mechanical_parts) > 0 and len(energy_levels) > 0 and len(built_drones) < 5:
    mechanical_part = mechanical_parts.pop()
    energy_level = energy_levels.popleft()

    drone_assembled = False
    sum = mechanical_part + energy_level

    for drone, value in drones.items():
        if sum >= value and drone not in built_drones:
            drone_assembled = True
            # Not exact match, but the next most suitable
            if sum > value:
                energy_level -= 30
                if energy_level > 0:
                    energy_levels.append(energy_level)

            built_drones.append(drone)
            break

    if not drone_assembled:
        energy_level -= 1
        if energy_level > 0:
            energy_levels.append(energy_level)

if len(built_drones) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if len(built_drones) > 0:
    print(f"Assembled Drones: {', '.join(map(str, built_drones))}")

if len(mechanical_parts) > 0:
    mechanical_parts.reverse()
    print(f"Mechanical Parts: {', '.join(map(str, mechanical_parts))}")

if len(energy_levels) > 0:
    print(f"Power Cells: {', '.join(map(str, energy_levels))}")
