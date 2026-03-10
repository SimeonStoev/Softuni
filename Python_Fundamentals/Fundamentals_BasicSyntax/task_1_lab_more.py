number = input()

number_list = list()

for i in number:
    number_list.append(int(i))

number_list.sort(reverse=True)

for i in number_list:
    print(i, end="")