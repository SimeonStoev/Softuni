row, col = [int(i) for i in input().split()]

matrix = [[int(i) for i in input().split()] for _ in range(row)]
sub_matrix = []
max_sum = -999999

for row_index in range(row - 2):
    for col_index in range(col - 2):
        first_elem = matrix[row_index][col_index]
        second_elem = matrix[row_index][col_index + 1]
        third_elem = matrix[row_index][col_index + 2]
        fourth_elem = matrix[row_index + 1][col_index]
        fifth_elem = matrix[row_index + 1][col_index + 1]
        sixth_elem = matrix[row_index + 1][col_index + 2]
        seventh_elem = matrix[row_index + 2][col_index]
        eighth_elem = matrix[row_index + 2][col_index + 1]
        ninth_elem = matrix[row_index + 2][col_index + 2]
        sum_elems = first_elem + second_elem + third_elem + fourth_elem + fifth_elem + sixth_elem + seventh_elem + eighth_elem + ninth_elem

        if sum_elems > max_sum:
            max_sum = sum_elems
            sub_matrix = [[first_elem, second_elem, third_elem], [fourth_elem, fifth_elem, sixth_elem],
                          [seventh_elem, eighth_elem, ninth_elem]]

print(f"Sum = {max_sum}")
for index in range(3):
    print(f"{' '.join(map(str, sub_matrix[index]))}")
