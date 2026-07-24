def type_check(var_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if isinstance(args[0], var_type):
                return function(*args, **kwargs)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
