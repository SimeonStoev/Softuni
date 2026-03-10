import re

string = input()

pattern = r"(?<!\S)[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@(?:[A-Za-z]+(?:-[A-Za-z]+)*\.)+[A-Za-z]+(?!-)"

matches = re.finditer(pattern, string)
for match in matches:
    print(match.group())