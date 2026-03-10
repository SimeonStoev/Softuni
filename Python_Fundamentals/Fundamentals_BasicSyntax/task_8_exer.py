command = ""
cups_of_coffee = 0

while command != "END":
    command = input()
    if command != "END":
        if command.lower() in ["coding", "cat", "dog", "movie"]:
            if 65 <= ord(command[0]) <= 90:
                cups_of_coffee += 2
            else:
                cups_of_coffee += 1

if cups_of_coffee > 5:
    print("You need extra sleep")
else:
    print(cups_of_coffee)