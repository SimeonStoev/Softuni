def age_assignment(*args, **kwargs):
    people = {}
    result_dict = {}
    result = ""
    for arg in args:
        people[arg[0]] = arg

    for key, value in kwargs.items():
        result_dict[people[key]] = value

    for key, value in dict(sorted(result_dict.items(), key=lambda x: x[0])).items():
        result += f"{key} is {value} years old.\n"

    return result
