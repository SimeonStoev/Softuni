import functools


def even_numbers(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [number for number in result if number % 2 == 0]
    return wrapper

@even_numbers
def get_numbers(numbers):
    """Some docs here"""
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
print(get_numbers.__name__, get_numbers.__doc__)
