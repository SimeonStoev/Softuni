array = [int(x) for x in input().split(" ")]

command = input()

while command != "end":
    command = command.split(" ")
    if command[0] == "swap":
        array[int(command[1])], array[int(command[2])] = array[int(command[2])], array[int(command[1])]
    elif command[0] == "multiply":
        array[int(command[1])] *= array[int(command[2])]
    elif command[0] == "decrease":
        array = [x - 1 for x in array]

    command = input()

output_array = ", ".join(map(str, array))
print(output_array)
