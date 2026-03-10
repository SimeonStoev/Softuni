string = input()
products = string.split("|")
budget = float(input())
first_budget = budget

products_for_sale = []
profit = 0

for elem in products:
    product = elem.split("->")
    if budget - float(product[1]) >= 0:
        if (product[0] == "Clothes" and float(product[1]) <= 50) or (
                product[0] == "Shoes" and float(product[1]) <= 35) or (
                product[0] == "Accessories" and float(product[1]) <= 20.50):
            budget -= float(product[1])
            products_for_sale.append(float(product[1]) * 1.4)
            profit += float(product[1]) * 0.4

for sold_products in products_for_sale:
    print(f"{sold_products:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")
if first_budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
