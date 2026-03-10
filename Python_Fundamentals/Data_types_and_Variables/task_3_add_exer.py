key = int(input())
lines = int(input())
decrypted_string = ""

for i in range(1, lines + 1):
    char = input()
    decrypted_string += chr(ord(char) + key)

print(decrypted_string)
