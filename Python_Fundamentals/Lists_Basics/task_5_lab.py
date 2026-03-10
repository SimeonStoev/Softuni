n = int(input())
list_of_ints = []
for i in range(n):
    number = int(input())
    list_of_ints.append(number)

command = input()

if command == "even":
    for index in range(len(list_of_ints) - 1, -1, -1):
        elem = list_of_ints[index]
        if elem % 2 != 0:
            list_of_ints.remove(elem)
elif command == "odd":
    for index in range(len(list_of_ints) - 1, -1, -1):
        elem = list_of_ints[index]
        if elem % 2 == 0:
            list_of_ints.remove(elem)
elif command == "negative":
    for index in range(len(list_of_ints) - 1, -1, -1):
        elem = list_of_ints[index]
        if elem >= 0:
            list_of_ints.remove(elem)
else:
    for index in range(len(list_of_ints) - 1, -1, -1):
        elem = list_of_ints[index]
        if elem < 0:
            list_of_ints.remove(elem)

print(list_of_ints)