vaucher_sum = float(input())
purchase = ""
purchase_sum = 0
number_of_tickets = 0
number_of_other_stocks = 0

while purchase != "End" and purchase_sum <= vaucher_sum:
    purchase = input()
    if purchase != "End":
        if len(purchase) > 8:
            purchase_sum += ord(purchase[0]) + ord(purchase[1])
            if purchase_sum <= vaucher_sum:
                number_of_tickets += 1
        else:
            purchase_sum += ord(purchase[0])
            if purchase_sum <= vaucher_sum:
                number_of_other_stocks += 1

print(number_of_tickets)
print(number_of_other_stocks)
