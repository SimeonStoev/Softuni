from collections import deque

chocolates = [int(chocolate) for chocolate in input().split(",")]
cups_of_milk = deque([int(cup_milk) for cup_milk in input().split(",")])
milk_shakes = 0

while len(chocolates) != 0 and len(cups_of_milk) != 0 and milk_shakes < 5:
    chocolate = 0
    while chocolate <= 0 and len(chocolates) != 0:
        chocolate = chocolates.pop()

    cup_of_milk = 0
    while cup_of_milk <= 0 and len(cups_of_milk) != 0:
        cup_of_milk = cups_of_milk.popleft()

    if chocolate > 0 and cup_of_milk > 0:
        if chocolate == cup_of_milk:
            milk_shakes += 1
        else:
            cups_of_milk.append(cup_of_milk)
            chocolates.append(chocolate - 5)
    else:
        if chocolate > 0:
            chocolates.append(chocolate)
        if cup_of_milk > 0:
            cups_of_milk.appendleft(cup_of_milk)

if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates) > 0:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")