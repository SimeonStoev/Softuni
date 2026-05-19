row, col = [int(x) for x in input().split()]

matrix = []
double_matrix_count = 0

for _ in range(row):
    matrix.append([x for x in input().split()])

for row_index in range(row - 1):
    for col_index in range(col - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] == \
                matrix[row_index + 1][col_index + 1]:
            double_matrix_count += 1

print(double_matrix_count)
