n = int(input())
word = input()
list_of_strings = []

for i in range(n):
    string = input()
    list_of_strings.append(string)

print(list_of_strings)

for index in range(len(list_of_strings) - 1, -1, -1):
    elem = list_of_strings[index]
    if word not in elem:
        list_of_strings.remove(elem)

print(list_of_strings)