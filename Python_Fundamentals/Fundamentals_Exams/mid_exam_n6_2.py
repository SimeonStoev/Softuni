treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split(" ")
    if command[0] == "Loot":
        new_loots = [loot for loot in command[1:] if loot not in treasure_chest]
        if len(new_loots) > 0:
            for loot in new_loots:
                treasure_chest.insert(0, loot)
    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(treasure_chest):
            loot = treasure_chest[int(command[1])]
            treasure_chest.remove(loot)
            treasure_chest.append(loot)
    elif command[0] == "Steal":
        treasure_chest_len = len(treasure_chest)
        if int(command[1]) > treasure_chest_len:
            command[1] = str(treasure_chest_len)
        removed_loots = treasure_chest[treasure_chest_len - int(command[1]):treasure_chest_len]
        treasure_chest = treasure_chest[:treasure_chest_len - int(command[1])]
        print(f"{', '.join(map(str, removed_loots))}")
    command = input()

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    avg_loots_length = sum([len(loot) for loot in treasure_chest]) / len(treasure_chest)
    print(f"Average treasure gain: {avg_loots_length:.2f} pirate credits.")
