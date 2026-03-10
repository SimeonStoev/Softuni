neighborhood = [int(x) for x in input().split("@")]
curr_pos = 0
command = input()

while command != "Love!":
    command = command.split(" ")
    step = int(command[1])
    if curr_pos + step < len(neighborhood):
        curr_pos += step
    else:
        curr_pos = 0

    if neighborhood[curr_pos] == 0:
        print(f"Place {curr_pos} already had Valentine's day.")
    else:
        neighborhood[curr_pos] -= 2
        if neighborhood[curr_pos] == 0:
            print(f"Place {curr_pos} has Valentine's day.")

    command = input()

houses_without_valent_day = len([x for x in neighborhood if x > 0])
print(f"Cupid's last position was {curr_pos}.")
if houses_without_valent_day > 0:
    print(f"Cupid has failed {houses_without_valent_day} places.")
else:
    print("Mission was successful.")
