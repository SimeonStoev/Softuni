n = int(input())
curr_volume = 0

for i in range(n):
    liters = int(input())
    if curr_volume + liters > 255:
        print("Insufficient capacity!")
    else:
        curr_volume += liters

print(curr_volume)