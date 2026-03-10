input_string_list = input().split(" ")
result_string = ""

for elem in input_string_list:
    ansii_numbs = [numb for numb in elem if numb.isdigit()]
    ansii_symbol = chr(int("".join(ansii_numbs)))

    string_list = list(elem[len(ansii_numbs):])
    t1 = string_list[-1]
    string_list[-1] = string_list[0]
    string_list[0] = t1

    result_string += ansii_symbol + "".join(string_list) + " "

print(result_string)
