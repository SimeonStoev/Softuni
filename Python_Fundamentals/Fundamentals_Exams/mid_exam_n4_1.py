food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000

not_enough_products = False

for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= pig_weight * (1 / 3)

    if food <= 0 or hay <= 0 or cover <= 0:
        not_enough_products = True
        break

if not_enough_products:
    print("Merry must go to the pet store!")
else:
    print(
        f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
