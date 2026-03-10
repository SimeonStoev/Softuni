def is_cell_valid(arr, x, y):
    return 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == "." and visited_map[x][y] == False


def get_dot_count(arr, i, j):
    result = 0
    if arr[i][j] == ".":
        result = 1
        visited_map[i][j] = True
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in dir:
            x = i + d[0]
            y = j + d[1]
            if is_cell_valid(arr, x, y):
                result += get_dot_count(arr, x, y)

    return result


n = int(input())
dot_map = []

for row in range(n):
    dot_map.append(input().split(" "))

visited_map = [[False for i in range(len(dot_map[0]))] for j in range(n)]

largest_count_of_dots = 0
for row in range(n):
    for col in range(len(dot_map[row])):
        curr_count_of_dots = get_dot_count(dot_map, row, col)
        if largest_count_of_dots < curr_count_of_dots:
            largest_count_of_dots = curr_count_of_dots

print(largest_count_of_dots)
