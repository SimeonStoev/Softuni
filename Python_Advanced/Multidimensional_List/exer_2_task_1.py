list_of_lists = input().split("|")
matrix_rows = len(list_of_lists)
matrix = [[int(x) for x in list_of_lists[index].split()] for index in range(matrix_rows)]

matrix.reverse()
result_list = []

for matrix_row in matrix:
    result_list.extend(matrix_row)

print(" ".join(map(str, result_list)))
