string_list = input().split()
sum = 0

for string in string_list:
    first_letter = string[0]
    first_letter_pos = ord(first_letter.lower()) - ord("a") + 1
    last_letter = string[len(string) - 1]
    last_letter_pos = ord(last_letter.lower()) - ord("a") + 1
    number = int(string[1: len(string) - 1])

    if first_letter == first_letter.upper():
        number /= first_letter_pos
    else:
        number *= first_letter_pos

    if last_letter == last_letter.upper():
        number -= last_letter_pos
    else:
        number += last_letter_pos

    sum += number

print(f"{sum:.2f}")
