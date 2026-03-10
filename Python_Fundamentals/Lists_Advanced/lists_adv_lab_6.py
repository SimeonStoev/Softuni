numbers = list(map(int, input().split(", ")))
found_indeces_or_no = list(map(lambda x: x if numbers[x] % 2 == 0 else "no",
                               range(len(numbers))
                               ))

result = list(filter(lambda x: x != "no", found_indeces_or_no))
print(result)
