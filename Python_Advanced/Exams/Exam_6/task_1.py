from collections import deque

money = [int(i) for i in input().split()]
prices = deque([int(i) for i in input().split()])

food_eaten = 0

while len(money) > 0 and len(prices) > 0:
    curr_money = money.pop()
    curr_price = prices.popleft()

    if curr_money == curr_price:
        food_eaten += 1
    elif curr_money > curr_price:
        food_eaten += 1
        difference = curr_money - curr_price
        if len(money) > 0:
            money[-1] += difference

if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif 0 < food_eaten < 4:
    food_eaten_print = (f"{food_eaten} foods." if food_eaten > 1 else f"{food_eaten} food.")
    print(f"Henry ate: {food_eaten_print}")
else:
    print("Henry remained hungry. He will try next weekend again.")
