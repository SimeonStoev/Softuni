line1 = input()
line2 = input()
line3 = input()
first_player_won = False
second_player_won = False

game = [line1.split(), line2.split(), line3.split()]

for row_index in range(len(game)):
    ones_count_row = 0
    twos_count_row = 0
    ones_count_col = 0
    twos_count_col = 0
    for column_index in range(len(game[row_index])):
        if game[row_index][column_index] == "1":
            ones_count_row += 1
        elif game[row_index][column_index] == "2":
            twos_count_row += 1

        if game[column_index][row_index] == "1":
            ones_count_col += 1
        elif game[column_index][row_index] == "2":
            twos_count_col += 1

    if ones_count_row == 3 or ones_count_col == 3:
        first_player_won = True
        break
    elif twos_count_row == 3 or twos_count_col == 3:
        second_player_won = True
        break

ones_count_diag = 0
twos_count_diag = 0
ones_count_diag_rev = 0
twos_count_diag_rev = 0
if not first_player_won or not second_player_won:
    for index in range(len(game)):
        if game[index][index] == "1":
            ones_count_diag += 1
        elif game[index][index] == "2":
            twos_count_diag += 1

        if game[index][len(game) - 1 - index] == "1":
            ones_count_diag_rev += 1
        elif game[index][len(game) - 1 - index] == "2":
            twos_count_diag_rev += 1

if ones_count_diag == 3 or ones_count_diag_rev == 3:
    first_player_won = True
elif twos_count_diag == 3 or twos_count_diag_rev == 3:
    second_player_won = True

winner = ""
if first_player_won:
    winner = "First"
elif second_player_won:
    winner = "Second"
else:
    winner = "Draw"

if winner != "Draw":
    print(f"{winner} player won")
else:
    print(f"{winner}!")
