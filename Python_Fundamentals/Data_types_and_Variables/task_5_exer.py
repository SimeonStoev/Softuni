start_char_number = int(input())
end_char_number = int(input())

for i in range(start_char_number, end_char_number + 1):
    print(chr(i), end=" ")
