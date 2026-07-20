def fibonacci():
    first, second = 0, 1
    yield 0
    yield 1
    current = first + second
    while True:
        yield current
        first, second = second, current
        current = first + second


generator = fibonacci()
for i in range(5):
    print(next(generator))
