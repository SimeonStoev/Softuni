def get_loading_bar(number):
    result = ""
    percent_number = number // 10

    if percent_number == 10:
        result = "100% Complete!\n[" + "%"*10 + "]"
    else:
        percent_numbers_left = 10 - percent_number
        bar = "%"*percent_number + "."*percent_numbers_left
        result = f"{number}% [{bar}]\nStill loading..."
    return result

numb = int(input())
print(get_loading_bar(numb))