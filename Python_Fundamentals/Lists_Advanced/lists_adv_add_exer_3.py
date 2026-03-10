def get_start_position(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == "k":
                return row, col
    return -1, -1


def is_cell_valid(arr, x, y):
    return (0 <= x < len(arr)) and (0 <= y < len(arr[0])) and (
            arr[x][y] == " " or arr[x][y] == "k") and visited_map[x][y] == False


def longest_path(arr, i, j):
    global exit_maze
    result = 0

    if is_cell_valid(arr, i, j):
        result = 1
        visited_map[i][j] = True
        if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[0]) - 1:
            exit_maze = True
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in dir:
            x = i + d[0]
            y = j + d[1]
            if is_cell_valid(arr, x, y):
                result += longest_path(arr, x, y)

    return result


def get_longest_path(arr):
    row_i, col_i = get_start_position(arr)
    return longest_path(arr, row_i, col_i)


rows = int(input())
maze = []
exit_maze = False

for index in range(rows):
    maze.append(list(map(str, input())))

visited_map = [[False for i in range(len(maze[0]))] for j in range(rows)]

moves_to_exit_maze = get_longest_path(maze)
if exit_maze:
    print(f"Kate got out in {moves_to_exit_maze} moves")
else:
    print("Kate cannot get out")
