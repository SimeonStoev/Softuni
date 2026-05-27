n = int(input())
matrix = []
a_r, a_c = -1, -1
number_of_teas = 0
went_to_the_party = False


def is_cell_valid(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(n):
    matrix_row = input().split()
    if "A" in matrix_row:
        a_r, a_c = i, matrix_row.index("A")
    matrix.append(matrix_row)

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    add_r, add_c = commands[command]
    matrix[a_r][a_c] = "*"
    a_r += add_r
    a_c += add_c
    if not is_cell_valid(a_r, a_c):
        break

    if matrix[a_r][a_c] == "R":
        matrix[a_r][a_c] = "*"
        break

    if matrix[a_r][a_c].isdigit():
        number_of_teas += int(matrix[a_r][a_c])

    if number_of_teas >= 10:
        went_to_the_party = True
        matrix[a_r][a_c] = "*"
        break

if went_to_the_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for i in range(n):
    print(" ".join(map(str, matrix[i])))
