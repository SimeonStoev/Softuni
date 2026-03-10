n = int(input())
is_even = True
odd_number = 0

for i in range(n):
    number = int(input())
    if number % 2 != 0:
        is_even = False
        odd_number = number
        break

if is_even:
    print("All numbers are even.")
else:
    print(f"{odd_number} is odd!")