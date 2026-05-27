from functools import reduce


def add_elems(*args):
    return reduce(lambda x, y: x + y, args)


def subtract_elems(*args):
    return reduce(lambda x, y: x - y, args)


def multiply_elems(*args):
    return reduce(lambda x, y: x * y, args)


def divide_elems(*args):
    return reduce(lambda x, y: x / y, args)


mapper = {
    "+": add_elems,
    "-": subtract_elems,
    "*": multiply_elems,
    "/": divide_elems
}


def operate(operation, *args):
    function = mapper[operation]
    return function(*args)
