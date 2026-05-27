def in_bounds(r_idx, c_idx, rows, cols):
    return 0 <= r_idx < rows and 0 <= c_idx < cols


def get_knight_coords(matrix):
    knight_coord = []
    for row_index in range(row):
        for col_index in range(col):
            if matrix[row_index][col_index] == 'K':
                current_knight_row = row_index
                current_knight_col = col_index
                current_knight_attacks = 0

                if in_bounds(current_knight_row - 2, current_knight_col - 1, row, col) and \
                        matrix[current_knight_row - 2][
                            current_knight_col - 1] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row - 2, current_knight_col + 1, row, col) and \
                        matrix[current_knight_row - 2][
                            current_knight_col + 1] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row - 1, current_knight_col - 2, row, col) and \
                        matrix[current_knight_row - 1][
                            current_knight_col - 2] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row - 1, current_knight_col + 2, row, col) and \
                        matrix[current_knight_row - 1][
                            current_knight_col + 2] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row + 1, current_knight_col - 2, row, col) and \
                        matrix[current_knight_row + 1][
                            current_knight_col - 2] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row + 1, current_knight_col + 2, row, col) and \
                        matrix[current_knight_row + 1][
                            current_knight_col + 2] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row + 2, current_knight_col - 1, row, col) and \
                        matrix[current_knight_row + 2][
                            current_knight_col - 1] == "K":
                    current_knight_attacks += 1
                if in_bounds(current_knight_row + 2, current_knight_col + 1, row, col) and \
                        matrix[current_knight_row + 2][
                            current_knight_col + 1] == "K":
                    current_knight_attacks += 1

                if current_knight_attacks > 0:
                    knight_coord.append([(current_knight_row, current_knight_col), current_knight_attacks])

    sorted_knight_coord = sorted(
        knight_coord,
        key=lambda x: (
            -x[1],  # по стойност низходящо
            x[0][0],
            x[0][1]
        )
    )

    return sorted_knight_coord


row = int(input())
col = row
chess_matrix = [[elem for elem in input()] for _ in range(row)]
number_of_knights_to_remove = 0

board_knight_coord = get_knight_coords(chess_matrix)

while len(board_knight_coord) > 0:
    knight = board_knight_coord[0]
    number_of_knights_to_remove += 1
    chess_matrix[knight[0][0]][knight[0][1]] = "0"
    board_knight_coord = get_knight_coords(chess_matrix)

print(number_of_knights_to_remove)
