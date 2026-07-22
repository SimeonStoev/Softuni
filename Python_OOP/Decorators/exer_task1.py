import functools


def logged(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        res = f"you called {function.__name__}{args}\n"
        res += f"it returned {result}"
        return res

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
