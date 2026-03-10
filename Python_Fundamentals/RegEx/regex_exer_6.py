import re

# www.internet.com"
pattern = r"www.[a-zA-Z0-9-]+(\.[a-z]+)+"

while True:
    try:
        sentence = input()
    except EOFError:
        break
    matches = re.finditer(pattern, sentence)
    for match in matches:
        print(match.group())