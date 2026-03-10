pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

command = input()

while command != "Retire":
    command = command.split(" ")
    if command[0] == "Fire":
        if 0 <= int(command[1]) < len(warship):
            warship[int(command[1])] -= int(command[2])
            if warship[int(command[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif command[0] == "Defend":
        if 0 <= int(command[1]) < len(pirate_ship) and 0 <= int(command[2]) < len(pirate_ship):
            pirate_ship_destroyed = False
            for index in range(int(command[1]), int(command[2]) + 1):
                pirate_ship[index] -= int(command[3])
                if pirate_ship[index] <= 0:
                    pirate_ship_destroyed = True
                    break
            if pirate_ship_destroyed:
                print("You lost! The pirate ship has sunken.")
                break
    elif command[0] == "Repair":
        if 0 <= int(command[1]) < len(pirate_ship):
            if pirate_ship[int(command[1])] + int(command[2]) > max_health:
                pirate_ship[int(command[1])] = max_health
            else:
                pirate_ship[int(command[1])] += int(command[2])
    elif command[0] == "Status":
        damaged_sections_count = len([x for x in pirate_ship if x < max_health * 0.2])
        print(f"{damaged_sections_count} sections need repair.")
    command = input()

if command == "Retire":
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
