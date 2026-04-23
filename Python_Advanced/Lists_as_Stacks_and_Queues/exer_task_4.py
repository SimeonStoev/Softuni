clothes = [int(x) for x in input().split()]
clothes_per_rack = int(input())

number_of_racks = 0
sum_for_curr_rack = 0

for _ in range(len(clothes)):
    clothe = clothes.pop()
    sum_for_curr_rack += clothe
    if sum_for_curr_rack > clothes_per_rack:
        number_of_racks += 1
        sum_for_curr_rack = clothe
    elif sum_for_curr_rack == clothes_per_rack:
        number_of_racks += 1
        sum_for_curr_rack = 0

if sum_for_curr_rack > 0:
    number_of_racks += 1

print(number_of_racks)
