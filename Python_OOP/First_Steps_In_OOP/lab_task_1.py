def print_rhombus_up(size):
    for i in range(size):
        print(" " * (size - i - 1) + "* " * (i + 1))

def print_rhombus_down(size):
    for i in range(size-1, 0, -1):
        print(" " * (size - i) + "* " * (i))

def print_rhombus(size):
    print_rhombus_up(size)
    print_rhombus_down(size)


n = int(input())

print_rhombus(n)