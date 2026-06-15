def is_cell_valid(x, y):
    return 0 <= x < size and 0 <= y < size


def restore_coordinates(x, y):
    if x == size:
        return 0, y
    if x == -1:
        return size - 1, y
    if y == -1:
        return x, size - 1
    if y == size:
        return x, 0

    return x, y


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

fishing_area = []
size = int(input())
# player coordinates
p_x, p_y = -1, -1
ship_catch = 0
NEEDED_CATCH = 20

for i in range(size):
    row = list(input())
    fishing_area.append(row)
    if "S" in row:
        p_x, p_y = i, row.index("S")
        fishing_area[p_x][p_y] = "-"

while True:
    command = input()
    if command == "collect the nets":
        break

    plus_x, plus_y = directions[command]
    p_x += plus_x
    p_y += plus_y

    if not is_cell_valid(p_x, p_y):
        p_x, p_y = restore_coordinates(p_x, p_y)

    if fishing_area[p_x][p_y] == "W":
        ship_catch = 0
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{p_x},{p_y}]")
        exit(0)

    if fishing_area[p_x][p_y].isdigit():
        ship_catch += int(fishing_area[p_x][p_y])
        fishing_area[p_x][p_y] = "-"

# mark ship position on the fishing area
fishing_area[p_x][p_y] = "S"

if ship_catch >= NEEDED_CATCH:
    print("Success! You managed to reach the quota!")
else:
    print(
        f"You didn't catch enough fish and didn't reach the quota! You need {NEEDED_CATCH - ship_catch} tons of fish more.")

if ship_catch > 0:
    print(f"Amount of fish caught: {ship_catch} tons.")

for i in range(size):
    print(''.join(fishing_area[i]))
