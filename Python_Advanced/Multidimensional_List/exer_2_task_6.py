n = 5
matrix = []
p_r, p_c = -1, -1
shot_targets = 0
all_targets = 0
targets_coords = []

for index in range(n):
    matrix_row = input().split()
    if "A" in matrix_row:
        p_r, p_c = index, matrix_row.index("A")
    if "x" in matrix_row:
        all_targets += sum(1 for i in matrix_row if i == "x")

    matrix.append(matrix_row)


def is_in_bounds(r, c):
    return 0 <= r < n and 0 <= c < n


def is_target_there(r, c):
    return matrix[r][c] == "x"


commands_count = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(commands_count):
    command = input().split()
    cmd = command[0]
    direction = command[1]
    n_r, n_c = directions[direction]
    if cmd == "move":
        steps = int(command[2])
        curr_r = p_r + n_r * steps
        curr_c = p_c + n_c * steps
        if is_in_bounds(curr_r, curr_c):
            if matrix[curr_r][curr_c] == ".":
                matrix[curr_r][curr_c] = "A"
                matrix[p_r][p_c] = "."
                p_r, p_c = curr_r, curr_c
    elif cmd == "shoot":
        curr_r = p_r + n_r
        curr_c = p_c + n_c
        while True:
            if not is_in_bounds(curr_r, curr_c):
                break
            if is_target_there(curr_r, curr_c):
                matrix[curr_r][curr_c] = "."
                shot_targets += 1
                targets_coords.append([curr_r, curr_c])
                break
            curr_r += n_r
            curr_c += n_c

    if shot_targets == all_targets:
        break

if shot_targets == all_targets:
    print(f"Training completed! All {shot_targets} targets hit.")
else:
    print(f"Training not completed! {all_targets - shot_targets} targets left.")

for target in targets_coords:
    print(target)
