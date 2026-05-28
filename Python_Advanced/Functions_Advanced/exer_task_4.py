def filter_even_numbers(*args):
    return list(filter(lambda x: x % 2 == 0, args))


def filter_odd_numbers(*args):
    return list(filter(lambda x: x % 2 != 0, args))


mapper = {
    "even": filter_even_numbers,
    "odd": filter_odd_numbers,
}


def even_odd_filter(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        function = mapper[key]
        number_list = function(*value)
        result_dict[key] = number_list
    return dict(sorted(result_dict.items(), key=lambda x: -len(x[1])))
