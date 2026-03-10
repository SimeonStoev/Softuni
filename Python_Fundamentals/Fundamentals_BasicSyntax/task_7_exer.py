command = ""

while command != "End":
    command = input()
    if command != "End" and command != "SoftUni":
        for letter in command:
            print(f"{letter}{letter}", end="")
        print()