numbers = tuple([float(x) for x in input().split()])
printed_numbers = []

for number in numbers:
    if number not in printed_numbers:
        printed_numbers.append(number)
        print(f"{number:.1f} - {numbers.count(number)} times")