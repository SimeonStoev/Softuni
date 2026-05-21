def is_command_valid(p_command, p_row, p_col):
    input_data = p_command.split()
    if len(input_data) == 5:
        comm = input_data[0]
        row_1 = input_data[1]
        col_1 = input_data[2]
        row_2 = input_data[3]
        col_2 = input_data[4]
        if comm == "swap" and row_1.isdigit() and col_1.isdigit() and row_2.isdigit() and col_2.isdigit():
            row_1, col_1, row_2, col_2 = int(row_1), int(col_1), int(row_2), int(col_2)
            if 0 <= row_1 < p_row and 0 <= row_2 < p_row and 0 <= col_1 < p_col and 0 <= col_2 < p_col:
                return row_1, col_1, row_2, col_2

    return False


row, col = [int(i) for i in input().split()]
matrix = [[x for x in input().split()] for _ in range(row)]

while True:
    command = input()

    if command == 'END':
        break

    if is_command_valid(command, row, col):
        x1, y1, x2, y2 = is_command_valid(command, row, col)
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
        for index in range(row):
            print(" ".join(map(str, matrix[index])))
    else:
        print("Invalid input!")
