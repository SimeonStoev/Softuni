divisor = int(input())
boundary = int(input())
largest_number = 0

for i in range(boundary, 0, -1):
    if i % divisor == 0:
        largest_number = i
        break

print(largest_number)