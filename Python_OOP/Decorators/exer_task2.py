import functools


def even_parameters(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
            return function(*args, **kwargs)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
