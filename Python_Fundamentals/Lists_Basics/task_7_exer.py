string = input()
gifts = string.split(" ")

command = input()

while command != "No Money":
    command_list = command.split(" ")
    if command_list[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == command_list[1]:
                gifts[index] = "None"
    elif command_list[0] == "Required":
        if 0 <= int(command_list[2]) < len(gifts) - 1:
            gifts[int(command_list[2])] = command_list[1]
    elif command_list[0] == "JustInCase":
        gifts[len(gifts) - 1] = command_list[1]
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")