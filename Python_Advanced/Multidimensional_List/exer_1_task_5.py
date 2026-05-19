row, col = [int(i) for i in input().split()]

matrix = []

for row_index in range(row):
    matrix_row = []
    for col_index in range(col):
        first_letter = chr(97 + row_index)
        second_letter = chr(97 + row_index + col_index)
        third_letter = chr(97 + row_index)
        matrix_row.append(first_letter + second_letter + third_letter)
    matrix.append(matrix_row)

for index in range(row):
    print(f"{' '.join(map(str, matrix[index]))}")
