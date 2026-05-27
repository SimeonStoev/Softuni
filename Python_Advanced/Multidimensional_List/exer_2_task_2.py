def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
cols = len(matrix[0]) if matrix else 0

while True:
    parts = input().split()
    cmd = parts[0]
    if cmd == "END":
        break

    r_idx, c_idx, val = map(int, parts[1:4])

    if not in_bounds(r_idx, c_idx, rows, cols):
        print("Invalid coordinates")
        continue

    if cmd == "Add":
        matrix[r_idx][c_idx] += val
    elif cmd == "Subtract":
        matrix[r_idx][c_idx] -= val
    # any other command is ignored (original code only expects Add/Subtract/END)

for row in matrix:
    print(" ".join(map(str, row)))
