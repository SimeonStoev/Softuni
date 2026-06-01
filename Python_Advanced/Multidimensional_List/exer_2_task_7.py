def is_cell_valid(m_row, m_col):
    return 0 <= m_row < n and 0 <= m_col < n


number_of_presents = int(input())
n = int(input())
santa_row, santa_col = -1, -1
good_kids_count = 0
matrix = []

for i in range(n):
    matrix_row = input().split()
    if "S" in matrix_row:
        santa_row, santa_col = i, matrix_row.index("S")
    good_kids_count += sum(1 for j in matrix_row if j == "V")
    matrix.append(matrix_row)

all_good_kids = good_kids_count

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
while True:
    command = input()
    if command == "Christmas morning":
        break

    row, col = direction[command]
    if not is_cell_valid(santa_row + row, santa_col + col):
        continue

    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = santa_row + row, santa_col + col
    if matrix[santa_row][santa_col] == "V":
        matrix[santa_row][santa_col] = "S"
        good_kids_count -= 1
        number_of_presents -= 1
        if number_of_presents == 0:
            break
    elif matrix[santa_row][santa_col] == "C":
        matrix[santa_row][santa_col] = "S"
        if matrix[santa_row - 1][santa_col] in ("V", "X"):
            number_of_presents -= 1
            if matrix[santa_row - 1][santa_col] == "V":
                good_kids_count -= 1
            matrix[santa_row - 1][santa_col] = "-"
            if number_of_presents == 0:
                break
        if matrix[santa_row + 1][santa_col] in ("V", "X"):
            number_of_presents -= 1
            if matrix[santa_row + 1][santa_col] == "V":
                good_kids_count -= 1
            matrix[santa_row + 1][santa_col] = "-"
            if number_of_presents == 0:
                break
        if matrix[santa_row][santa_col - 1] in ("V", "X"):
            number_of_presents -= 1
            if matrix[santa_row][santa_col - 1] == "V":
                good_kids_count -= 1
            matrix[santa_row][santa_col - 1] = "-"
            if number_of_presents == 0:
                break
        if matrix[santa_row][santa_col + 1] in ("V", "X"):
            number_of_presents -= 1
            if matrix[santa_row][santa_col + 1] == "V":
                good_kids_count -= 1
            matrix[santa_row][santa_col + 1] = "-"
            if number_of_presents == 0:
                break

if good_kids_count > 0 and number_of_presents == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(map(str, row)))

if good_kids_count == 0:
    print(f"Good job, Santa! {all_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")
