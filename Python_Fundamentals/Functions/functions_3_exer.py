def get_string_between(first, last):
    result = ""
    for i in range(ord(first) + 1, ord(last)):
        result += chr(i) + " "
    return result

char1 = input()
char2 = input()

print(get_string_between(char1, char2))