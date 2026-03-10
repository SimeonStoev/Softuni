def get_data_type_value(data_type, value):
    if data_type == "int":
        return int(value) * 2
    elif data_type == "real":
        result = f"{float(value) * 1.5:.2f}"
        return result
    else:
        return "$" + value + "$"

data_type_inp = input()
value_inp = input()
print(get_data_type_value(data_type_inp, value_inp))