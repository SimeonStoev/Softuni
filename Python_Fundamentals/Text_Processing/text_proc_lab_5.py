string = input()
numeric = ""
alpha = ""
others = ""

for char in string:
    if char.isdigit():
        numeric += char
    elif char.isalpha():
        alpha += char
    else:
        others += char

print(numeric)
print(alpha)
print(others)
