def sorting_cheeses(**kwargs):
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for elem in sorted_kwargs:
        result += f"{elem[0]}\n"
        for list_elem in sorted(elem[1], reverse=True):
            result += f"{list_elem}\n"

    return result
