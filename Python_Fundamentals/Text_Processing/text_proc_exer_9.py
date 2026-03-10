input_string = input()
result = ""
unique_chars = ""
curr_str_message = ""
repeat_number = ""

for index in range(len(input_string)):
    char = input_string[index]
    if char.isdigit():
        if index < len(input_string) - 1 and input_string[index + 1].isdigit():
            repeat_number += char
        else:
            repeat_number += char
            repeat_number = int(repeat_number)
            curr_str_message = curr_str_message.upper() * repeat_number
            result += curr_str_message
            curr_str_message = ""
            repeat_number = ""
    else:
        curr_str_message += char
        if char.upper() not in unique_chars:
            unique_chars += char.upper()

print(f"Unique symbols used: {len(unique_chars)}")
print(result)
