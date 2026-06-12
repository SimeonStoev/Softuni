def is_cell_valid(x, y):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split(", "))
ct_x, ct_y = -1, -1
ct_time = 16
bomb_defused = False
ct_killed = False
bomb_exploded = False
time_to_defuse_bomb = 0
matrix = []

for row in range(n):
    matrix_row = [char for char in input()]
    if "C" in matrix_row:
        ct_x, ct_y = row, matrix_row.index("C")
    matrix.append(matrix_row)

commands_coords = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
while not ct_killed and not bomb_defused and not bomb_exploded:
    
    if ct_time <= 0:
        bomb_exploded = True
        continue

    command = input()

    if command == "defuse":
        if matrix[ct_x][ct_y] != "B":
            ct_time -= 2
            continue

        time_left_to_defuse = ct_time - 4
        time_to_defuse_bomb = abs(time_left_to_defuse)
        if time_left_to_defuse >= 0:
            matrix[ct_x][ct_y] = "D"
            bomb_defused = True
            continue
        else:
            bomb_exploded = True
            matrix[ct_x][ct_y] = "X"
            continue
    else:
        plus_x, plus_y = commands_coords[command]
        if is_cell_valid(ct_x + plus_x, ct_y + plus_y):
            ct_x += plus_x
            ct_y += plus_y
            if matrix[ct_x][ct_y] == "T":
                ct_killed = True
                matrix[ct_x][ct_y] = "*"
                continue

        ct_time -= 1

if bomb_exploded:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {time_to_defuse_bomb} second/s.")
elif bomb_defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time_to_defuse_bomb} second/s remaining.")
elif ct_killed:
    print("Terrorists win!")

for row in matrix:
    print("".join(row))
