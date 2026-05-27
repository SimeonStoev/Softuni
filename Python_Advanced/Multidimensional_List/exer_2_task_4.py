rows = int(input())

matrix = []
br = bc = -1

for r in range(rows):
    row = input().split()
    if "B" in row:
        br, bc = r, row.index("B")
    matrix.append(row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < rows


best_sum = float("-inf")
best_path = []
best_dir = ""

for direction, (dr, dc) in directions.items():

    r, c = br, bc
    curr_sum = 0
    path = []

    while True:
        r += dr
        c += dc

        if not is_valid(r, c):
            break

        if matrix[r][c] == "X":
            break

        curr_sum += int(matrix[r][c])
        path.append([r, c])

    if path and curr_sum > best_sum:
        best_sum = curr_sum
        best_path = path
        best_dir = direction

if best_dir:
    print(best_dir)
for p in best_path:
    print(p)
print(best_sum)
