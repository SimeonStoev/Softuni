def func_executor(*args):
    result = ""
    for elem in args:
        function = elem[0]
        arguments = elem[1]
        result += f"{function.__name__} - {function(*arguments)}\n"
    return result
