n = int(input())
matrix = []

for _ in range(n):
    matrix_row = [x for x in input()]
    matrix.append(matrix_row)

symbol = input()

for row in range(n):
    for col in range(n):
        if symbol == matrix[row][col]:
            result = (row, col)
            print(result)
            exit()

print(f"{symbol} does not occur in the matrix")
