def squares(number):
    current = 1
    while current <= number:
        yield current * current
        current += 1


print(list(squares(5)))
