import math


def get_closest_point(x1, y1, x2, y2):
    z1 = math.pow(x1, 2) + math.pow(y1, 2)
    z2 = math.pow(x2, 2) + math.pow(y2, 2)

    result = ""
    if z1 > z2:
        result = f"({math.floor(x2)}, {math.floor(y2)})"
    else:
        result = f"({math.floor(x1)}, {math.floor(y1)})"

    return result

p_x1 = float(input())
p_y1 = float(input())
p_x2 = float(input())
p_y2 = float(input())
print(get_closest_point(p_x1, p_y1, p_x2, p_y2))