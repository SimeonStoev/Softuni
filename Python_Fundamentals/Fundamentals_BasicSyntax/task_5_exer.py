number_of_orders = int(input())

price_for_all_orders = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if (0.01 <= price_per_capsule <= 100) and (1 <= days <= 31) and (1 <= capsules <= 2000):
        price_for_order = 0
        price_for_order += price_per_capsule * days * capsules
        print(f"The price for the coffee is: ${price_for_order:.2f}")
        price_for_all_orders += price_for_order

print(f"Total: ${price_for_all_orders:.2f}")