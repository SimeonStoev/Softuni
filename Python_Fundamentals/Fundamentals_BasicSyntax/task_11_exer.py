budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price_for_liter = flour_price * 1.25
milk_price = milk_price_for_liter / 4

loave_price = flour_price + eggs_price + milk_price
curr_sum = 0

number_of_loaves = 0
number_of_eggs = 0

while curr_sum <= budget:
    curr_sum += loave_price
    if curr_sum <= budget:
        number_of_loaves += 1
        number_of_eggs += 3
        if number_of_loaves % 3 == 0:
            number_of_eggs -= (number_of_loaves - 2)

print(
    f"You made {number_of_loaves} loaves of Easter bread! Now you have {number_of_eggs} eggs and {budget - (curr_sum - loave_price):.2f}BGN left.")
