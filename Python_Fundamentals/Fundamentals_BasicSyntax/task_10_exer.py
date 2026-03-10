string_one = input()
string_two = input()

new_string = list(string_one)
printed_strings = [string_one]

for i in range(len(string_two)):
    new_string[i] = string_two[i]
    new_str = "".join(new_string)
    if new_str not in printed_strings:
        print(new_str)
        printed_strings.append(new_str)