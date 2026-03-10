import math


def print_factorial_division(num1, num2):
    print(f"{math.factorial(num1) / math.factorial(num2):.2f}")

number1 = int(input())
number2 = int(input())
print_factorial_division(number1, number2)