n = int(input())
plants = {}

for _ in range(n):
    string = input().split("<->")
    plant = string[0]
    rarity = string[1]
    if plant not in plants:
        plants[plant] = {"rarity": rarity, "rating": []}
    else:
        plants[plant]["rarity"] = rarity

while True:
    command = input()
    if command == "Exhibition":
        break

    command = command.split(": ")
    if command[0] == "Rate":
        plant_list = command[1].split()
        plant_name = plant_list[0]
        plant_rating = int(plant_list[2])
        if plant_name in plants:
            plants[plant_name]["rating"].append(plant_rating)
        else:
            print("error")
    elif command[0] == "Update":
        plant_list = command[1].split()
        plant_name = plant_list[0]
        plant_rarity = plant_list[2]
        if plant_name in plants:
            plants[plant_name]["rarity"] = plant_rarity
        else:
            print("error")
    elif command[0] == "Reset":
        plant_name = command[1]
        if plant_name in plants:
            plants[plant_name]["rating"] = []
        else:
            print("error")

print("Plants for the exhibition:")
for key, value in plants.items():
    plant_rating = sum(value["rating"])
    number_of_ratings = len(value["rating"])
    average_rating= 0
    if number_of_ratings > 0:
        average_rating = plant_rating / number_of_ratings
    else:
        average_rating = 0
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {average_rating:.2f}")
