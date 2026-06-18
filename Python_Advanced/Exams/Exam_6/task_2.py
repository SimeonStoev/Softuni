n = int(input())

airspace = []
jet_x, jet_y = -1, -1
jet_armour = 300
enemy_aircrafts = 4
jet_destroyed = False

for i in range(n):
    airspace_row = list(input())
    airspace.append(airspace_row)
    if "J" in airspace_row:
        jet_x, jet_y = i, airspace_row.index("J")
        airspace[jet_x][jet_y] = "-"

commands_direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    plus_x, plus_y = commands_direction[command]
    jet_x += plus_x
    jet_y += plus_y

    if airspace[jet_x][jet_y] == "E":
        airspace[jet_x][jet_y] = "-"
        enemy_aircrafts -= 1
        if enemy_aircrafts > 0:
            jet_armour -= 100
            if jet_armour <= 0:
                jet_destroyed = True
                break
        else:
            break

    if airspace[jet_x][jet_y] == "R":
        jet_armour = 300
        airspace[jet_x][jet_y] = "-"

airspace[jet_x][jet_y] = "J"

if jet_destroyed:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_x}, {jet_y}]!")
else:
    print("Mission accomplished, you neutralized the aerial threat!")

for i in range(n):
    print(f"{''.join(airspace[i])}")
