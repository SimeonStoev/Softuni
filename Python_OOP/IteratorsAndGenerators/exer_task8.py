def get_primes(numbers: list):
    for number in numbers:
        is_prime = True
        for numb in range(2, number):
            if number % numb == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            yield number


print(list(get_primes([-2, 0, 0, 1, 1, 0])))
