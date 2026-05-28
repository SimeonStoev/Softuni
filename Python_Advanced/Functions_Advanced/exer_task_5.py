def concatenate(*args, **kwargs):
    concat_args = ""
    for arg in args:
        concat_args += arg

    for key, value in kwargs.items():
        if key in concat_args:
            concat_args = concat_args.replace(key, value)

    return concat_args
