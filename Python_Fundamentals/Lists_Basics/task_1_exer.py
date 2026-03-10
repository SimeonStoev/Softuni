numbers = input()
list_numbers = numbers.split()
opposite_numbers = []

for number in list_numbers:
    opposite_numbers.append(int(number) * (-1))

print(opposite_numbers)

