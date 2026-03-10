numbers_list = list(map(int, input().split(", ")))
tuple_list = []

min_number = min(numbers_list)
max_number = max(numbers_list)
min_group = (min_number // 10) * 10
max_group = (max_number // 10) * 10
if min_number % 10 != 0:
    min_group += 10
if max_number % 10 != 0:
    max_group += 10

for number in numbers_list:
    group = (number // 10) * 10
    if number % 10 != 0:
        group += 10
    tuple_list.append((group, number))

for group in range(min_group, max_group + 1, 10):
    result_list = []
    for tup in tuple_list:
        if tup[0] == group:
            result_list.append(tup[1])
    print(f"Group of {group}'s: {result_list}")
