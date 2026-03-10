first_char_ascii = ord(input())
second_char_ascii = ord(input())
string = input()
ascii_sum = 0

for char in string:
    if first_char_ascii < ord(char) < second_char_ascii:
        ascii_sum += ord(char)

print(ascii_sum)
