integer_list = input()
numbers_to_remove = int(input())

integers = [int(x) for x in integer_list.split(" ")]
integers_sort = [int(x) for x in integer_list.split(" ")]
integers_sort.sort()
numbs_to_remove = integers_sort[:numbers_to_remove]

for index in range(len(integers) - 1, -1, -1):
    if integers[index] in numbs_to_remove:
        integers.pop(index)


last_index = len(integers) - 1
for index in range(len(integers)):
    if index < last_index:
        print(integers[index], end=", ")
    else:
        print(integers[index], end="")