rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

matrix_diagonal_sum = 0
matrix_reverse_diagonal_sum = 0

for index in range(rows):
    matrix_diagonal_sum += matrix[index][index]
    matrix_reverse_diagonal_sum += matrix[index][rows - 1 - index]

print(abs(matrix_diagonal_sum - matrix_reverse_diagonal_sum))
