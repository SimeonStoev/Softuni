def print_tribonacci_numbers(number):
    a, b, c = 1, 1, 2
    tribonacci_numbers = []

    for i in range(number):
       tribonacci_numbers.append(str(a))
       a, b, c = b, c, a+b+c

    print(" ".join(tribonacci_numbers))

n = int(input())
print_tribonacci_numbers(n)