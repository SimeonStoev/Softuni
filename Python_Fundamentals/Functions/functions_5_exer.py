def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

numbers = [int(number) for number in input().split()]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)