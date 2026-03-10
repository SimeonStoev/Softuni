string = input()
len_string = len(string)
index = 0
add_power = 0
result_string = ""

while index < len_string:
    if string[index] != ">":
        result_string += string[index]
        index += 1
    elif string[index] == ">":
        result_string += string[index]
        power = int(string[index + 1])
        end_index = -1
        if add_power != 0:
            power += add_power
            add_power = 0

        substr_to_remove = string[index + 1:index + power + 1]
        if ">" in substr_to_remove:
            end_index = substr_to_remove.index(">") + 1
            add_power = power - end_index + 1
        else:
            end_index = power + 1

        index += end_index

print(result_string)
