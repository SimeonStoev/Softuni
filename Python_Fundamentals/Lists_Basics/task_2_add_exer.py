number_sequence = input()
string = list(input())

number_list = number_sequence.split(' ')
message = ""

for i in range(len(number_list)):
    index = 0
    for number in number_list[i]:
        index += int(number)
    number_list[i] = int(index)

for index in number_list:
    position = 0
    string_length = len(string)
    if int(index) < string_length:
        position = int(index)
    else:
        position = int(index) % string_length

    message += string[position]
    string.pop(position)

print(message)
