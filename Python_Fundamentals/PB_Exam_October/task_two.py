tshirt_price = float(input())
sum_needed_for_the_ball = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.20
sport_shoes_price = (tshirt_price + shorts_price) * 2

# sum without discount
sum = tshirt_price + socks_price + sport_shoes_price + shorts_price
# sum with 15 % discount
sum_with_discount = sum * 0.85

if sum_with_discount >= sum_needed_for_the_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_with_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_needed_for_the_ball - sum_with_discount:.2f} lv. more.")