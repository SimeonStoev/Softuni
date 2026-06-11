def print_triangle_upper_part(size):
    for i in range(1, size+1):
        row = [j for j in range(1, i+1)]
        print(*row)

def print_triangle_lower_part(size):
    for i in range(size-1, 0, -1):
        row = [j for j in range(1, i+1)]
        print(*row)

def print_triangle(size):
    print_triangle_upper_part(size)
    print_triangle_lower_part(size)