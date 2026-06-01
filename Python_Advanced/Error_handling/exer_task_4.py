class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def is_square_matrix(matrix):
    matrix_length = len(matrix)
    for i in range(matrix_length):
        if len(matrix[i]) != matrix_length:
            return False

    return True


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:
    line = input().split()

    if not line:
        break

    try:
        line = [int(x) for x in line]
    except ValueError:
        raise MatrixContentError("The matrix must consist of only integers")

    mtrx.append(line)

if len(mtrx) == 0 or not is_square_matrix(mtrx):
    raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
