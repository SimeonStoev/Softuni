def is_cell_valid(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())

maze = []
p_x, p_y = -1, -1
player_health = 100
MAX_HEALTH = 100

commands_direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    maze_row = list(input())
    maze.append(maze_row)
    if "P" in maze_row:
        p_x, p_y = i, maze_row.index("P")
        maze[p_x][p_y] = "-"

while True:
    command = input()
    plus_x, plus_y = commands_direction[command]

    # If player new coordinates are invalid, skip the command
    if not is_cell_valid(p_x + plus_x, p_y + plus_y):
        continue

    # Player new coordinates
    p_x += plus_x
    p_y += plus_y

    # Player faces a monster and loses health points
    if maze[p_x][p_y] == "M":
        player_health -= 40
        if player_health <= 0:
            player_health = 0
            break

        maze[p_x][p_y] = "-"

    # Player boost new health points
    if maze[p_x][p_y] == "H":
        player_health = min(MAX_HEALTH, player_health + 15)
        maze[p_x][p_y] = "-"

    # Player exits the maze
    if maze[p_x][p_y] == "X":
        break

# Set the last known position of player in the maze
maze[p_x][p_y] = "P"

if player_health == 0:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {player_health} units")

for i in range(n):
    print(f"{''.join(maze[i])}")
