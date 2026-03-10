string = list(input())
numbers = [int(number) for number in string if number in "0123456789"]
characters = [char for char in string if char not in "0123456789"]

take_list = [numbers[index] for index in range(len(numbers)) if index % 2 == 0]
skip_list = [numbers[index] for index in range(len(numbers)) if index % 2 != 0]

result_string = ""

for index in range(len(take_list)):
    result_string += "".join(characters[:take_list[index]])
    characters = characters[take_list[index]:]
    characters = characters[skip_list[index]:]

print(result_string)
