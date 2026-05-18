row, col = [int(x) for x in input().split(", ")]
matrix = []
biggest_sub_matrix = []
biggest_sum = -999999999

for _ in range(row):
    matrix_row = [int(x) for x in input().split(", ")]
    matrix.append(matrix_row)

for row_index in range(row - 1):
    for col_index in range(col - 1):
        first_elem = matrix[row_index][col_index]
        second_elem = matrix[row_index][col_index + 1]
        third_elem = matrix[row_index + 1][col_index]
        fourth_elem = matrix[row_index + 1][col_index + 1]
        curr_sum = first_elem + second_elem + third_elem + fourth_elem

        if curr_sum > biggest_sum:
            biggest_sum = curr_sum
            biggest_sub_matrix = [[first_elem, second_elem], [third_elem, fourth_elem]]

print(*biggest_sub_matrix[0])
print(*biggest_sub_matrix[1])
print(biggest_sum)
