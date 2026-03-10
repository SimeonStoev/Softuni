targets = [int(x) for x in input().split(" ")]

command = input()

while command != "End":
    command = command.split(" ")
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if 0 <= index - radius < len(targets) and 0 <= index + radius < len(targets):
            targets = targets[:index - radius] + targets[index + radius + 1:]
        else:
            print("Strike missed!")

    command = input()

result = "|".join(map(str, targets))
print(result)
