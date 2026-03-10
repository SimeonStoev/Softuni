lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
sum_to_repair = 0
shields_broken = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        sum_to_repair += helmet_price
    if fight % 3 == 0:
        sum_to_repair += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        sum_to_repair += shield_price
        shields_broken += 1
        if shields_broken % 2 == 0:
            sum_to_repair += armor_price

print(f"Gladiator expenses: {sum_to_repair:.2f} aureus")
