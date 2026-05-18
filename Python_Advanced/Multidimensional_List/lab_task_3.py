rows = int(input())
flattered_matrix = []

for _ in range(rows):
    matrix_row = [int(x) for x in input().split(", ")]
    flattered_matrix.extend(matrix_row)

print(flattered_matrix)
