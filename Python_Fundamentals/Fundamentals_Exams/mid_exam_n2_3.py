numbers = [int(x) for x in input().split(" ")]

average_number = sum(numbers) / len(numbers)

greater_numbers = [x for x in numbers if x > average_number]

greater_numbers = sorted(greater_numbers, reverse=True)

if len(greater_numbers) == 0:
    print("No")
else:
    result = " ".join(map(str, greater_numbers[:5]))
    print(result)
