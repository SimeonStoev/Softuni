smallest_number = lambda num1, num2, num3: min(num1, min(num2, num3))

a = int(input())
b = int(input())
c = int(input())
print(smallest_number(a, b, c))