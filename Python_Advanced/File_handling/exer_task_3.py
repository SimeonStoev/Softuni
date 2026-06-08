import os
from traceback import print_tb

import Constants

file_path = os.path.join(Constants.path_to_dir, "Files")

while True:
    command = input()
    if command == "End":
        break

    command = command.split("-")
    if command[0] == "Create":
        file_name = command[1]
        with open(os.path.join(file_path, file_name), "w") as file:
            file.write("")
    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(os.path.join(file_path, file_name), "a") as file:
            file.write(content + "\n")
    elif command[0] == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        try:
            with open(os.path.join(file_path, file_name), "r") as file:
                file_content = file.read()
                file_content = file_content.replace(old_string, new_string)
                with open(os.path.join(file_path, file_name), "w") as file:
                    file.write(file_content)
        except FileNotFoundError:
            print("An error occurred")
    elif command[0] == "Delete":
        file_name = command[1]
        try:
            os.remove(os.path.join(file_path, file_name))
        except FileNotFoundError:
            print("An error occurred")
