clothes = [int(x) for x in input().split()]
clothes_per_rack = int(input())

number_of_racks = 0
sum_for_curr_rack = 0

# Process each clothing item from the stack (LIFO)
while clothes:
    item = clothes.pop()
    sum_for_curr_rack += item

    if sum_for_curr_rack > clothes_per_rack:
        # Current item exceeds capacity, start new rack
        number_of_racks += 1
        sum_for_curr_rack = item
    elif sum_for_curr_rack == clothes_per_rack:
        # Rack is exactly full, move to next rack
        number_of_racks += 1
        sum_for_curr_rack = 0

# Count the last rack if it has items
if sum_for_curr_rack > 0:
    number_of_racks += 1

print(number_of_racks)
