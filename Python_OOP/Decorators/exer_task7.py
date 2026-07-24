import functools
import os


def store_results(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        path = os.path.abspath(__file__)
        path_to_dir = os.path.dirname(path)
        path_to_file = os.path.join(path_to_dir, "Files")
        try:
            result = function(*args, **kwargs)
            with open(os.path.join(path_to_file, "results.txt"), "a") as f:
                f.write(f"Function {function.__name__} was called. Result: {result}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
