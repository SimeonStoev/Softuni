n1 = int(input())
n2 = int(input())
n3 = int(input())

max_number = n1

if max_number < n2:
    max_number = n2

if max_number < n3:
    max_number = n3

print(max_number)