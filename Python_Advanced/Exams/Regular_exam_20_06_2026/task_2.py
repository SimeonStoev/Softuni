def is_cell_valid(x, y):
    return 0 <= x < n and 0 <= y < n


def restore_coordinates(x, y):
    if x < 0:
        return (n - 1, y)
    if x == n:
        return (0, y)
    if y < 0:
        return (x, n - 1)
    if y == n:
        return (x, 0)

    return (x, y)


commands_direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())
matrix = []
s_x, s_y = -1, -1
ship_durability = 100
MAX_DURABILITY = 100
all_treasure_count = 0
treasure_count = 0
used_charm = False

for i in range(n):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if "S" in matrix_row:
        s_x, s_y = i, matrix_row.index("S")
        matrix[s_x][s_y] = "."
    all_treasure_count += matrix_row.count("*")

while True:
    command = input()

    if command == "stop":
        break

    plus_x, plus_y = commands_direction[command]
    s_x += plus_x
    s_y += plus_y

    if not is_cell_valid(s_x, s_y):
        s_x, s_y = restore_coordinates(s_x, s_y)

    if matrix[s_x][s_y] == "*":
        treasure_count += 1
        matrix[s_x][s_y] = "."
        if treasure_count == all_treasure_count:
            break
    elif matrix[s_x][s_y] == "C":
        if not used_charm:
            ship_durability = (ship_durability + 25 if ship_durability + 25 <= MAX_DURABILITY else MAX_DURABILITY)
            used_charm = True
        matrix[s_x][s_y] = "."
    elif matrix[s_x][s_y] == "M":
        ship_durability -= 25
        matrix[s_x][s_y] = "."
        if ship_durability <= 0:
            break

matrix[s_x][s_y] = "S"
ship_durability = (0 if ship_durability <= 0 else ship_durability)

if ship_durability == 0:
    print(f"Shipwreck! Last known coordinates ({s_x}, {s_y})")
elif treasure_count == all_treasure_count:
    print("Yo-ho-ho! All treasure chests collected!")
else:
    print("Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {ship_durability}")

if treasure_count < all_treasure_count:
    print(f"Unclaimed chests: {all_treasure_count - treasure_count}")

for row in matrix:
    print("".join(row))
