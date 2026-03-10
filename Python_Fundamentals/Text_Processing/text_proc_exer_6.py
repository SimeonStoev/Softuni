string = input()
formated_string = ""
last_char = ""

for index in range(len(string)):
    current_char = string[index]
    if current_char != last_char:
        last_char = string[index]
        formated_string += current_char

print(formated_string)
