rows, cols = [int(index) for index in input().split(", ")]
matrix = []
sum_of_elems = 0

for _ in range(rows):
    matrix_row = [int(x) for x in input().split(", ")]
    sum_of_elems += sum(matrix_row)
    matrix.append(matrix_row)

print(sum_of_elems)
print(matrix)