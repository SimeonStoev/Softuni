movie = input()
hall_type = input()
number_of_sold_tickets = int(input())
income = 0

if movie == "A Star Is Born":
    if hall_type == "normal":
        income = number_of_sold_tickets * 7.5
    elif hall_type == "luxury":
        income = number_of_sold_tickets * 10.5
    else:
        income = number_of_sold_tickets * 13.5
elif movie == "Bohemian Rhapsody":
    if hall_type == "normal":
        income = number_of_sold_tickets * 7.35
    elif hall_type == "luxury":
        income = number_of_sold_tickets * 9.45
    else:
        income = number_of_sold_tickets * 12.75
elif movie == "Green Book":
    if hall_type == "normal":
        income = number_of_sold_tickets * 8.15
    elif hall_type == "luxury":
        income = number_of_sold_tickets * 10.25
    else:
        income = number_of_sold_tickets * 13.25
else:
    if hall_type == "normal":
        income = number_of_sold_tickets * 8.75
    elif hall_type == "luxury":
        income = number_of_sold_tickets * 11.55
    else:
        income = number_of_sold_tickets * 13.95

print(f"{movie} -> {income:.2f} lv.")
