string = input()
encrypted_string = ""

for char in string:
    encrypted_string += chr(ord(char) + 3)

print(encrypted_string)
