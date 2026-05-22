row = int(input())
commands = input().split()
matrix = []
number_of_coals = 0
curr_position = [-1, -1]

for row_index in range(row):
    matrix_row = input().split()
    matrix.append(matrix_row)
    if "s" in matrix_row and curr_position[0] == -1:
        curr_position = [row_index, matrix_row.index("s")]
    number_of_coals += sum(1 for element in matrix_row if element == "c")

for command in commands:
    ignore_command = False
    if command == "left" and curr_position[1] > 0:
        matrix[curr_position[0]][curr_position[1]] = "*"
        curr_position[1] -= 1
    elif command == "right" and curr_position[1] < row - 1:
        matrix[curr_position[0]][curr_position[1]] = "*"
        curr_position[1] += 1
    elif command == "up" and curr_position[0] > 0:
        matrix[curr_position[0]][curr_position[1]] = "*"
        curr_position[0] -= 1
    elif command == "down" and curr_position[0] < row - 1:
        matrix[curr_position[0]][curr_position[1]] = "*"
        curr_position[0] += 1
    else:
        ignore_command = True

    if not ignore_command:
        if matrix[curr_position[0]][curr_position[1]] == "c":
            number_of_coals -= 1
            if number_of_coals == 0:
                print(f"You collected all coal! ({curr_position[0]}, {curr_position[1]})")
                exit()
        if matrix[curr_position[0]][curr_position[1]] == "e":
            print(f"Game over! ({curr_position[0]}, {curr_position[1]})")
            exit()

print(f"{number_of_coals} pieces of coal left. ({curr_position[0]}, {curr_position[1]})")
