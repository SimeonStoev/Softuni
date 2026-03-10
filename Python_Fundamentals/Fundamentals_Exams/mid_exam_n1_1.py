comp_part_price = input()
total_price = 0

while comp_part_price not in ("special", "regular"):
    comp_part_price = float(comp_part_price)
    if comp_part_price < 0:
        print("Invalid price!")
    else:
        total_price += comp_part_price

    comp_part_price = input()

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    total_price_with_taxes = 0
    if comp_part_price == "special":
        total_price_with_taxes =  (total_price + taxes) * 0.9
    else:
        total_price_with_taxes = total_price + taxes

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")

