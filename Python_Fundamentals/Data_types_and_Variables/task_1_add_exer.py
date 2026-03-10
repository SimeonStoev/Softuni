a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")
container = a
a = b
b = container
print("After:")
print(f"a = {a}")
print(f"b = {b}")
