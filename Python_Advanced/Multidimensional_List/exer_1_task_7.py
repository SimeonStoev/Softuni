from itertools import cycle

row, col = [int(i) for i in input().split()]
matrix = [[" " for _ in range(col)] for _ in range(row)]
snake = input()
snake_cycle = cycle(snake)

for row_index in range(row):
    col_range = range(col) if row_index % 2 == 0 else range(col - 1, -1, -1)
    for col_index in col_range:
        matrix[row_index][col_index] = next(snake_cycle)

for row in matrix:
    print("".join(row))
