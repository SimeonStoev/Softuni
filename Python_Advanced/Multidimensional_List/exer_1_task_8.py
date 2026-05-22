rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
cols = len(matrix[0]) if matrix else 0

bombs = input().split()

for bomb_pos in bombs:
    x, y = (int(n) for n in bomb_pos.split(','))
    bomb = matrix[x][y]
    if bomb <= 0:
        continue
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > 0:
                matrix[nx][ny] -= bomb
    matrix[x][y] = 0

alive_cells = sum(1 for r in matrix for v in r if v > 0)
alive_sum = sum(v for r in matrix for v in r if v > 0)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")
for r in matrix:
    print(" ".join(map(str, r)))
