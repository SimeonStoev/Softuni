def grocery_store(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: ((-x[1], -len(x[0])), x[0])))
    result = ""
    for key, value in sorted_dict.items():
        result += f"{key}: {value}\n"
    return result
