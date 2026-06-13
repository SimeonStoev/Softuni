def list_roman_emperors(*args, **kwargs):
    number_of_emperors = len(args)
    succ_emperors = {emp: 0 for emp, is_succ in args if is_succ}
    unsucc_emperors = {emp: 0 for emp, is_succ in args if not is_succ}

    for emp, years in kwargs.items():
        if emp in succ_emperors:
            succ_emperors[emp] = years
        elif emp in unsucc_emperors:
            unsucc_emperors[emp] = years

    sorted_succ_emperors = dict(sorted(succ_emperors.items(), key=lambda x: (-x[1], x[0])))
    sorted_unsucc_emperors = dict(sorted(unsucc_emperors.items(), key=lambda x: (x[1], x[0])))

    result = f"Total number of emperors: {number_of_emperors}\n"

    if len(sorted_succ_emperors) > 0:
        result += "Successful emperors:\n"
        for emp, years in sorted_succ_emperors.items():
            result += f"****{emp}: {years}\n"

    if len(sorted_unsucc_emperors) > 0:
        result += "Unsuccessful emperors:\n"
        for emp, years in sorted_unsucc_emperors.items():
            result += f"****{emp}: {years}\n"

    return result
