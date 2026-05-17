from collections import deque


def founded_colors_denormalize(colors):
    denorm_colors = colors
    if "orange" in colors and ("red" not in colors or "yellow" not in colors):
        denorm_colors.remove("orange")
    if "purple" in colors and ("red" not in colors or "blue" not in colors):
        denorm_colors.remove("purple")
    if "green" in colors and ("yellow" not in colors or "blue" not in colors):
        denorm_colors.remove("green")

    return denorm_colors


input_string = deque([string for string in input().split()])

main_colors = ("red", "yellow", "blue")
secondary_colors = ("orange", "purple", "green")

founded_colors = []

while len(input_string) > 0:
    first = input_string.popleft()
    if len(input_string) > 0:
        last = input_string.pop()
    else:
        last = ""

    check_color = first + last
    check_color_reverse = last + first
    if check_color in main_colors or check_color in secondary_colors:
        founded_colors.append(check_color)
    elif check_color_reverse in main_colors or check_color_reverse in secondary_colors:
        founded_colors.append(check_color_reverse)
    else:
        first = first[:len(first) - 1]
        last = last[:len(last) - 1]
        mid_index = len(input_string) // 2
        insert_first_index_ok = False
        if len(first) > 0:
            input_string.insert(mid_index, first)
            insert_first_index_ok = True
        if len(last) > 0:
            if insert_first_index_ok:
                mid_index += 1
            input_string.insert(mid_index, last)

founded_colors_denorm = founded_colors_denormalize(founded_colors)

print(founded_colors_denorm)
