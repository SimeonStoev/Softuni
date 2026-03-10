string = input()
events = string.split("|")
initial_energy = 100
initial_coins = 100
all_events_completed = True

for elem in events:
    event = elem.split("-")
    if event[0] == "rest":
        prev_initial_energy = initial_energy
        gained_energy = int(event[1])
        initial_energy += int(event[1])
        if initial_energy > 100:
            initial_energy = 100
            gained_energy = 100 - prev_initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event[0] == "order":
        if initial_energy - 30 < 0:
            initial_energy += 50
            print("You had to rest!")
        else:
            initial_coins += int(event[1])
            initial_energy -= 30
            print(f"You earned {int(event[1])} coins.")
    else:
        if initial_coins - int(event[1]) >= 0:
            initial_coins -= int(event[1])
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            all_events_completed = False
            break

if all_events_completed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

