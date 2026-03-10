budget = int(input())
price_per_product = 0

while price_per_product != "End" and budget >= 0:
    price_per_product = input()
    if price_per_product != "End":
        budget -= int(price_per_product)

if budget >= 0:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")