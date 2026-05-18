row = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(row)]

#for _ in range(row):
#    matrix_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
#    matrix.append(matrix_row)

print(matrix)