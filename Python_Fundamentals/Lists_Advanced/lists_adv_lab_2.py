number_of_wagons = int(input())
train = [0] * number_of_wagons
command = input()

while command != 'End':
    command_list = command.split()
    if command_list[0] == 'add':
        train[number_of_wagons - 1] += int(command_list[1])
    elif command_list[0] == 'insert':
        train[int(command_list[1])] += int(command_list[2])
    else:
        train[int(command_list[1])] -= int(command_list[2])

    command = input()

print(train)
