rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

matrix_diagonal = []
matrix_diagonal_sum = 0
matrix_reverse_diagonal = []
matrix_reverse_diagonal_sum = 0

for index in range(rows):
    matrix_diagonal.append(matrix[index][index])
    matrix_diagonal_sum += matrix[index][index]
    matrix_reverse_diagonal.append(matrix[index][rows - 1 - index])
    matrix_reverse_diagonal_sum += matrix[index][rows - 1 - index]

print(
    f"Primary diagonal: {', '.join(map(str, matrix_diagonal))}. Sum: {matrix_diagonal_sum} \nSecondary diagonal: {', '.join(map(str, matrix_reverse_diagonal))}. Sum: {matrix_reverse_diagonal_sum}")
