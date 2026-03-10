def check_list_for_palyndromes(numb_list):
    numbers = numb_list.split(", ")
    for number in numbers:
        if int(number) == int(number[::-1]):
            print(True)
        else:
            print(False)

number_list = input()
check_list_for_palyndromes(number_list)