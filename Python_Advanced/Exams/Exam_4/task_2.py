def is_cell_valid(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


n = int(input())

matrix = []
p_x, p_y = -1, -1
player_stars = 2

commands_direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    matrix_row = input().split()
    matrix.append(matrix_row)
    if "P" in matrix_row:
        p_x, p_y = i, matrix_row.index("P")
        matrix[p_x][p_y] = "."

while 0 < player_stars < 10:
    command = input()
    plus_x, plus_y = commands_direction[command]
    if not is_cell_valid(p_x + plus_x, p_y + plus_y):
        p_x, p_y = 0, 0
    else:
        p_x += plus_x
        p_y += plus_y

    if matrix[p_x][p_y] == "*":
        player_stars += 1
        matrix[p_x][p_y] = "."
    elif matrix[p_x][p_y] == "#":
        player_stars -= 1
        p_x -= plus_x
        p_y -= plus_y

matrix[p_x][p_y] = "P"

if player_stars == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{p_x}, {p_y}]")

for i in range(n):
    print(*matrix[i])
