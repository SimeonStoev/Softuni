import math


def get_primes(numbers: list):
    for number in numbers:
        if number > 1 and all(number % i != 0 for i in range(2, math.isqrt(number) + 1)):
            yield number


print(list(get_primes([-2, 0, 0, 1, 1, 0])))
