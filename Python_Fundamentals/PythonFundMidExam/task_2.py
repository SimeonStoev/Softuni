def get_new_position(p_city_grid, start_pos, steps, direction):
    new_pos_index = start_pos
    curr_steps = 0
    if direction == "Step Backward":
        while curr_steps < steps:
            curr_steps += 1
            new_pos_index = new_pos_index - 1
            if new_pos_index < 0:
                new_pos_index = len(p_city_grid) - 1
    else:
        while curr_steps < steps:
            curr_steps += 1
            new_pos_index = new_pos_index + 1
            if new_pos_index >= len(p_city_grid):
                new_pos_index = 0

    return new_pos_index


city_grid = [int(elem) for elem in input().split("|")]
collected_items = 0
command = input()

while command != "Adventure over":
    if "$" in command:
        command = command.split("$")
        curr_pos = int(command[1])
        curr_command = command[0]
        steps_to_move = int(command[2])
        if 0 <= curr_pos <= len(city_grid) - 1:
            new_pos = get_new_position(city_grid, curr_pos, steps_to_move, curr_command)
            collected_items += city_grid[new_pos]
            city_grid[new_pos] = 0

    else:
        command = command.split()
        if command[0] == "Double":
            if 0 <= int(command[1]) < len(city_grid):
                city_grid[int(command[1])] *= 2
        else:
            city_grid.reverse()

    command = input()

result_city_grid = " - ".join(map(str, city_grid))
print(result_city_grid)
print(f"Robo finished the adventure with {collected_items} items!")
