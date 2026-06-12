def print_matrix():
    global matrix
    for row in matrix:
        print(''.join(row))


def is_cell_valid(x, y):
    return 0 <= x < n and 0 <= y < n


def extend_row_and_column_index(x, y):
    if x == -1:
        return (n - 1, y)
    if y == -1:
        return (x, n - 1)
    if x == n:
        return (0, y)
    if y == n:
        return (x, 0)


n = int(input())
matrix = []
bee_x, bee_y = 0, 0
bee_energy = 15
collected_nectar = 0
restore_energy = True

for row in range(n):
    matrix_row = [char for char in input()]
    matrix.append(matrix_row)

    if "B" in matrix_row:
        col = matrix_row.index("B")
        bee_x, bee_y = row, col
        matrix[row][col] = "-"

command_dict = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    # Bee new coordinates, depending on direction
    plus_x, plus_y = command_dict[command]
    bee_x += plus_x
    bee_y += plus_y

    # Cut bee energy by 1
    bee_energy -= 1

    # If bee goes out of matrix, it is positioned on the other part of the matrix
    if not is_cell_valid(bee_x, bee_y):
        bee_x, bee_y = extend_row_and_column_index(bee_x, bee_y)

    # if the is flower at the bee cell
    if matrix[bee_x][bee_y].isdigit():
        collected_nectar += int(matrix[bee_x][bee_y])
        matrix[bee_x][bee_y] = "-"

    # Bee reached the hive and the loop ends
    if matrix[bee_x][bee_y] == "H":
        matrix[bee_x][bee_y] = "B"
        break

    # Check if bee energy is enough to continue
    if bee_energy == 0:
        if collected_nectar < 30 or not restore_energy:
            matrix[bee_x][bee_y] = "B"
            print("This is the end! Beesy ran out of energy.")
            print_matrix()
            exit(0)

        if restore_energy:
            energy_to_restore = collected_nectar - 30
            bee_energy = energy_to_restore
            collected_nectar = 30
            restore_energy = False

if collected_nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
else:
    print("Beesy did not manage to collect enough nectar.")

print_matrix()
