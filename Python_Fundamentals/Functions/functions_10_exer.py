def is_perfect_number(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor

    return sum_of_divisors == number

numb = int(input())
if is_perfect_number(numb):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")