def is_cell_valid(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())

matrix = []
p_x, p_y = -1, -1
player_money = 100
win_jackpot = False

commands_direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if "G" in matrix_row:
        p_x, p_y = i, matrix_row.index("G")
        matrix[p_x][p_y] = "-"

while True:
    command = input()

    if command == "end":
        break

    plus_x, plus_y = commands_direction[command]

    if not is_cell_valid(p_x + plus_x, p_y + plus_y):
        play_again = 0
        break

    p_x += plus_x
    p_y += plus_y

    if matrix[p_x][p_y] in ("W", "P", "J"):

        if matrix[p_x][p_y] == "W":
            player_money += 100
        elif matrix[p_x][p_y] == "J":
            player_money += 100000
            win_jackpot = True
        elif matrix[p_x][p_y] == "P":
            player_money -= 200

        matrix[p_x][p_y] = "-"

    if player_money <= 0 or win_jackpot:
        break

matrix[p_x][p_y] = "G"

if player_money <= 0:
    print("Game over! You lost everything!")
elif win_jackpot:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {player_money}$")
else:
    print(f"End of the game. Total amount: {player_money}$")

if player_money > 0:
    for row in matrix:
        print("".join(row))
