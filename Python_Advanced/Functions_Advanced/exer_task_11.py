def math_operations(*args, **kwargs):
    row_arg = 0
    for arg in args:
        row_arg += 1
        if row_arg == 1:
            kwargs["a"] += arg
        elif row_arg == 2:
            kwargs["s"] -= arg
        elif row_arg == 3:
            if arg != 0:
                kwargs["d"] /= arg
        else:
            kwargs["m"] *= arg
            row_arg = 0

    sorted_dict = dict(sorted(kwargs.items(), key=lambda item: (-item[1], item[0])))

    result = ""

    for key, value in sorted_dict.items():
        result += f"{key}: {value:.1f}\n"

    return result
