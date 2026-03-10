import re

numbers = []

pattern = r"(^|(?<=.))\d+((?=.)|$)"


while True:
    try:
        text = input()
    except EOFError:
        break
    matches = re.finditer(pattern, text)
    for match in matches:
        numbers.append(match.group())

print(" ".join(numbers))