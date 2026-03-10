string = input()
integer_list = string.split()
command = input()

while command != "end":
    # do something
    command_list = command.split()
    if command_list[0] == "exchange":
        if int(command_list[1]) >= len(integer_list) or int(command_list[1]) < 0:
            print("Invalid index")
        else:
            first_list = []
            second_list = []
            for index in range(int(command_list[1]) + 1):
                first_list.append(integer_list[index])
            for index in range(int(command_list[1]) + 1, len(integer_list)):
                second_list.append(integer_list[index])
            integer_list = second_list + first_list
    elif command_list[0] == "max":
        max_elem = -1
        max_index = -1
        for index in range(len(integer_list)):
            if command_list[1] == "even" and int(integer_list[index]) % 2 == 0:
                if max_elem <= int(integer_list[index]):
                    max_elem = int(integer_list[index])
                    max_index = index
            elif command_list[1] == "odd" and int(integer_list[index]) % 2 != 0:
                if max_elem <= int(integer_list[index]):
                    max_elem = int(integer_list[index])
                    max_index = index
        if max_index != -1:
            print(max_index)
        else:
            print("No matches")
    elif command_list[0] == "min":
        min_elem = 1001
        min_index = 51
        for index in range(len(integer_list)):
            if command_list[1] == "even" and int(integer_list[index]) % 2 == 0:
                if min_elem >= int(integer_list[index]):
                    min_elem = int(integer_list[index])
                    min_index = index
            elif command_list[1] == "odd" and int(integer_list[index]) % 2 != 0:
                if min_elem >= int(integer_list[index]):
                    min_elem = int(integer_list[index])
                    min_index = index
        if min_index != 51:
            print(min_index)
        else:
            print("No matches")
    elif command_list[0] == "first":
        if int(command_list[1]) > len(integer_list):
            print("Invalid count")
        else:
            index = 0
            counter = 0
            result_list = []
            while counter < int(command_list[1]) and index < len(integer_list):
                if command_list[2] == "even" and int(integer_list[index]) % 2 == 0:
                    result_list.append(integer_list[index])
                    counter += 1
                elif command_list[2] == "odd" and int(integer_list[index]) % 2 != 0:
                    result_list.append(integer_list[index])
                    counter += 1
                index += 1
            print("[", end="")
            for i in range(len(result_list)):
                if i < len(result_list) - 1:
                    print(result_list[i], end=", ")
                else:
                    print(result_list[i], end="")
            print("]")
    elif command_list[0] == "last":
        if int(command_list[1]) > len(integer_list):
            print("Invalid count")
        else:
            index = len(integer_list) - 1
            counter = 0
            result_list = []
            while counter < int(command_list[1]) and index >= 0:
                if command_list[2] == "even" and int(integer_list[index]) % 2 == 0:
                    result_list.append(integer_list[index])
                    counter += 1
                elif command_list[2] == "odd" and int(integer_list[index]) % 2 != 0:
                    result_list.append(integer_list[index])
                    counter += 1
                index -= 1
            result_list.reverse()
            print("[", end="")
            for i in range(len(result_list)):
                if i < len(result_list) - 1:
                    print(result_list[i], end=", ")
                else:
                    print(result_list[i], end="")
            print("]")

    command = input()

print("[", end="")
for i in range(len(integer_list)):
    if i < len(integer_list) - 1:
        print(integer_list[i], end=", ")
    else:
        print(integer_list[i], end="]")
