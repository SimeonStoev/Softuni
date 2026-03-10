string = input()
capitalized_list = list()
index = 0

for i in string:
    if 65 <= ord(i) <= 90:
        capitalized_list.append(index)
    index += 1

print(capitalized_list)