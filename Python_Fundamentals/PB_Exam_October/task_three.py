number_of_dancers = int(input())
points = float(input())
season = input()
country = input()

win_price = number_of_dancers * points
net_win_price = 0
sum_for_charity = 0
sum_for_the_band = 0

if country == "Abroad":
    win_price += win_price * 0.5
    if season == "summer":
        net_win_price = win_price - win_price * 0.1
    else:
        net_win_price = win_price - win_price * 0.15
else:
    if season == "summer":
        net_win_price = win_price - win_price * 0.05
    else:
        net_win_price = win_price - win_price * 0.08

sum_for_charity = net_win_price * 0.75
sum_for_the_band = net_win_price - sum_for_charity

print(f"Charity - {sum_for_charity:.2f}")
print(f"Money per dancer - {sum_for_the_band / number_of_dancers:.2f}")