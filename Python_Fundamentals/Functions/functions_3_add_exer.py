import math


def get_distince_to_zero_point(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

def get_distance_between_points(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def print_points_with_bigger_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    distance_first_pair_points = get_distance_between_points(x1, y1, x2, y2)
    distance_second_pair_points = get_distance_between_points(x3, y3, x4, y4)
    print(f"distance_first_pair_points: {distance_first_pair_points}")
    print(f"distance_second_pair_points: {distance_second_pair_points}")

    if distance_first_pair_points >= distance_second_pair_points:
        if get_distince_to_zero_point(x1, y1) <= get_distince_to_zero_point(x2, y2):
            print(f"({math.ceil(x1)}, {math.ceil(y1)})({math.ceil(x2)}, {math.ceil(y2)})")
        else:
            print(f"({math.ceil(x2)}, {math.ceil(y2)})({math.ceil(x1)}, {math.ceil(y1)})")
    else:
        if get_distince_to_zero_point(x3, y3) <= get_distince_to_zero_point(x4, y4):
            print(f"({math.ceil(x3)}, {math.ceil(y3)})({math.ceil(x4)}, {math.ceil(y4)})")
        else:
            print(f"({math.ceil(x4)}, {math.ceil(y4)})({math.ceil(x3)}, {math.ceil(y3)})")

p1_x = float(input())
p1_y = float(input())
p2_x = float(input())
p2_y = float(input())
p3_x = float(input())
p3_y = float(input())
p4_x = float(input())
p4_y = float(input())
print_points_with_bigger_distance(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y)