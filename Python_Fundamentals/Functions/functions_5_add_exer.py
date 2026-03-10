def get_numb_type_list(n1, n2, n3):
    numb_type_list = []
    number_of_positive = 0
    number_of_negative = 0
    zeros = 0
    if n1 > 0:
        number_of_positive += 1
    else:
        if n1 == 0:
            zeros += 1
        else:
            number_of_negative += 1
    if n2 > 0:
        number_of_positive += 1
    else:
        if n2 == 0:
            zeros += 1
        else:
            number_of_negative += 1
    if n3 > 0:
        number_of_positive += 1
    else:
        if n3 == 0:
            zeros += 1
        else:
            number_of_negative += 1
    
    numb_type_list = [number_of_positive, number_of_negative, zeros]
    return numb_type_list

def is_positive(numbs_type_list):
    if numbs_type_list[0] == 3 or (numbs_type_list[0] == 1 and numbs_type_list[1] == 2):
        return True
    else:
        return False

def is_negative(numbs_type_list):
    if numbs_type_list[1] == 3 or (numbs_type_list[1] == 1 and numbs_type_list[0] == 2):
        return True
    else:
        return False

def is_zero(numbs_type_list):
    if numbs_type_list[2] > 0:
        return True
    else:
        return False

number1 = int(input())
number2 = int(input())
number3 = int(input())
numbers_type_list = get_numb_type_list(number1, number2, number3)
if is_positive(numbers_type_list):
    print("positive")
elif is_negative(numbers_type_list):
    print("negative")
else:
    print("zero")