budget = float(input())
number_of_statist = int(input())
clothes_for_statist_price = float(input())
decor = budget * 0.1
expenses = 0

if number_of_statist > 150:
    clothes_for_statist_price -= clothes_for_statist_price * 0.1

expenses = decor + number_of_statist * clothes_for_statist_price

if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")
