string = input()

while True:
    command = input()
    if command == "Finalize":
        break

    command = command.split()
    if command[0] == "Encrypt":
        string = string[::-1]
        print(string)
    elif command[0] == "Decrypt":
        string = string.swapcase()
        print(string)
    elif command[0] == "Substitute":
        old_char = command[1]
        new_char = command[2]
        if old_char not in string:
            print("Character not found.")
        else:
            string = string.replace(old_char, new_char)
            print(string)
    elif command[0] == "Scramble":
        index = int(command[1])
        char = command[2]
        if 0 <= index < len(string):
            if index == len(string) - 1:
                string = string[:index] + char
            else:
                string = string[:index] + char + string[index + 1:]
            print(string)
        else:
            print("Index out of bounds.")
    elif command[0] == "Remove":
        substring = command[1]
        string = string.replace(substring, "")
        print(string)
    else:
        print("Invalid command detected!")
