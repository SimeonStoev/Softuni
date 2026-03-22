def is_valid_index(index, list_length):
    return 0 <= index < list_length

world_tour_stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if is_valid_index(index, len(world_tour_stops)):
            world_tour_stops = world_tour_stops[:index] + string + world_tour_stops[index:]
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if is_valid_index(start_index, len(world_tour_stops)) and is_valid_index(end_index, len(world_tour_stops)) and start_index <= end_index:
            world_tour_stops = world_tour_stops[:start_index] + world_tour_stops[end_index+1:]
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in world_tour_stops:
            world_tour_stops = world_tour_stops.replace(old_string, new_string)

    print(world_tour_stops)

print(f"Ready for world tour! Planned stops: {world_tour_stops}")