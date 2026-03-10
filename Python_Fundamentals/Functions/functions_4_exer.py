def get_odd_and_even_sum(numb):
    even_sum = 0
    odd_sum = 0
    for digit in str(numb):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = int(input())
print(get_odd_and_even_sum(number))