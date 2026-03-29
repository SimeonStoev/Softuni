animals = {}
areas = {}

while True:
    command = input()
    if command == "EndDay":
        break

    command = command.split(": ")
    if command[0] == "Add":
        animal_data = command[1].split("-")
        animal = animal_data[0]
        food = int(animal_data[1])
        area = animal_data[2]
        if animal in animals:
            animals[animal]["food"] += food
        else:
            animals[animal] = {"food": food, "area": area}
    elif command[0] == "Feed":
        animal_data = command[1].split("-")
        animal = animal_data[0]
        food = int(animal_data[1])
        if animal in animals:
            animals[animal]["food"] -= food
            if animals[animal]["food"] <= 0:
                animals.pop(animal)
                print(f"{animal} was successfully fed")

for animal_data in animals.values():
    if animal_data["area"] in areas:
        areas[animal_data["area"]] += 1
    else:
        areas[animal_data["area"]] = 1

print("Animals:")
for animal in animals.keys():
    print(f" {animal} -> {animals[animal]['food']}g")

print("Areas with hungry animals:")
for key, value in areas.items():
    print(f"{key}: {value}")
