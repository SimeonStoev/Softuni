def filter_even(*args):
    return [x for x in args if x % 2 == 0]


def filter_odd(*args):
    return [x for x in args if x % 2 != 0]


mapper = {'even': filter_even, 'odd': filter_odd}


def even_odd(*args):
    command = args[-1]
    numbers = args[:len(args) - 1]
    function = mapper[command]
    return function(*numbers)
