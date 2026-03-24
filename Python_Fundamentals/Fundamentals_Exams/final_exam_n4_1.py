raw_password = input()

while True:
    command = input()
    if command == "Done":
        break

    command = command.split()
    if command[0] == "TakeOdd":
        raw_password = "".join([raw_password[index] for index in range(1, len(raw_password), 2)])
        print(raw_password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        raw_password = raw_password[:index] + raw_password[index + length:]
        print(raw_password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitution = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitution)
            print(raw_password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {raw_password}")
