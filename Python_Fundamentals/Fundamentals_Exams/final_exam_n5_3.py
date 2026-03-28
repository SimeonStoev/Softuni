cities = {}

while True:
    city_data = input()
    if city_data == "Sail":
        break

    city_data = city_data.split("||")
    city = city_data[0]
    population = int(city_data[1])
    gold = int(city_data[2])
    if city in cities:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    else:
        cities[city] = {"population": population, "gold": gold}

while True:
    command = input()
    if command == "End":
        break

    command = command.split("=>")
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])

        if gold >= 0:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
