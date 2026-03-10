tourists = int(input())
lift_wagons = [int(x) for x in input().split(" ")]
index = 0

for wagon in lift_wagons:
    free_spaces = 4 - wagon
    if free_spaces > 0:
        if tourists - free_spaces < 0:
            lift_wagons[index] += tourists
            tourists = 0
        else:
            tourists -= free_spaces
            lift_wagons[index] += free_spaces

        if tourists == 0:
            break

    index += 1

if tourists == 0 and sum(lift_wagons) < len(lift_wagons) * 4:
    print("The lift has empty spots!")
elif tourists > 0:
    print(f"There isn't enough space! {tourists} people in a queue!")

for wagon in lift_wagons:
    print(f"{wagon} ", end="")
