numbers_list = list(map(int, input().split(", ")))
positive_numbers_list = [number for number in numbers_list if number >= 0]
negative_numbers_list = [number for number in numbers_list if number < 0]
even_numbers_list = [number for number in numbers_list if number % 2 == 0]
odd_numbers_lists = [number for number in numbers_list if number % 2 != 0]

print(f"Positive: ", end="")
for index in range(len(positive_numbers_list)):
    if index < len(positive_numbers_list) - 1:
        print(positive_numbers_list[index], end=", ")
    else:
        print(positive_numbers_list[index], end="")
print()
print(f"Negative: ", end="")
for index in range(len(negative_numbers_list)):
    if index < len(negative_numbers_list) - 1:
        print(negative_numbers_list[index], end=", ")
    else:
        print(negative_numbers_list[index], end="")
print()
print(f"Even: ", end="")
for index in range(len(even_numbers_list)):
    if index < len(even_numbers_list) - 1:
        print(even_numbers_list[index], end=", ")
    else:
        print(even_numbers_list[index], end="")
print()
print(f"Odd: ", end="")
for index in range(len(odd_numbers_lists)):
    if index < len(odd_numbers_lists) - 1:
        print(odd_numbers_lists[index], end=", ")
    else:
        print(odd_numbers_lists[index], end="")
