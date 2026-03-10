rooms = input().split("|")
best_room = 0
health = 100
bitcoins = 0

for room in rooms:
    best_room += 1
    room = room.split(" ")
    if room[0] == "potion":
        heal_points = int(room[1])
        if heal_points + health > 100:
            heal_points = 100 - health
        health += heal_points
        print(f"You healed for {heal_points} hp.")
        print(f"Current health: {health} hp.")
    elif room[0] == "chest":
        bitcoins += int(room[1])
        print(f"You found {int(room[1])} bitcoins.")
    else:
        health -= int(room[1])
        if health > 0:
            print(f"You slayed {room[0]}.")
        else:
            print(f"You died! Killed by {room[0]}.")
            print(f"Best room: {best_room}")
            break

if health > 0:
    result = f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}"
    print(result)
