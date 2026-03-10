qunatity = int(input())
days_until_christmas = int(input())
budget = 0
christmas_points = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        qunatity += 2

    if day % 2 == 0:
        budget += qunatity * 2
        christmas_points += 5
    if day % 3 == 0:
        budget += qunatity * 5 + qunatity * 3
        christmas_points += 3 + 10
    if day % 5 == 0:
        budget += qunatity * 15
        christmas_points += 17
    if day % 3 == 0 and day % 5 == 0:
        christmas_points += 30

    if day % 10 == 0:
        christmas_points -= 20
        budget += 23

if days_until_christmas % 10 == 0:
    christmas_points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_points}")
