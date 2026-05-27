import copy

rows, cols = map(int, input().split())


def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols


def expand_bunnies(matrix):
    original = copy.deepcopy(matrix)
    player_captured = False
    for r in range(rows):
        for c in range(cols):
            if original[r][c] == "B":
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        if matrix[nr][nc] == "P":
                            player_captured = True
                        matrix[nr][nc] = "B"
    return player_captured


matrix = []
player_row, player_col = -1, -1
for i in range(rows):
    row = list(input())
    matrix.append(row)
    if "P" in row:
        player_row, player_col = i, row.index("P")

commands = input()
player_won = player_captured = False
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for cmd in commands:
    if cmd not in directions:
        continue

    dr, dc = directions[cmd]
    nr, nc = player_row + dr, player_col + dc

    matrix[player_row][player_col] = "."
    if not is_valid(nr, nc):
        player_won = True
    elif matrix[nr][nc] == "B":
        player_captured = True
        player_row, player_col = nr, nc
    else:
        matrix[nr][nc] = "P"
        player_row, player_col = nr, nc

    if expand_bunnies(matrix):
        player_captured = True

    if player_won or player_captured:
        break

for row in matrix:
    print("".join(row))

status = "won" if player_won else "dead"
print(f"{status}: {player_row} {player_col}")
