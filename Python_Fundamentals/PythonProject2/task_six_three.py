number_of_clients = int(input())
sum_all = 0

for i in range(number_of_clients):
    product = ""
    sum = 0
    number_of_products = 0
    while product != "Finish":
        product = input()
        if product != "Finish":
            number_of_products += 1
            if product == "basket":
                sum += 1.5
            elif product == "wreath":
                sum += 3.8
            else:
                sum += 7
                
    if number_of_products % 2 == 0:
        sum -= sum * 0.2
    print(f"You purchased {number_of_products} items for {sum:.2f} leva.")

    sum_all += sum

print(f"Average bill per client is: {sum_all / number_of_clients:.2f} leva.")
