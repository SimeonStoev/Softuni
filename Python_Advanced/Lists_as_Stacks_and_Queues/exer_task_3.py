from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)
is_food_enough = True
print(biggest_order)

while len(orders) > 0:
    order = orders.popleft()
    if food - order < 0:
        is_food_enough = False
        orders.appendleft(order)
        break
    food -= order

if is_food_enough:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders))}")
