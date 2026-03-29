import re

pattern = r"(@|#)+([a-z]{3,})(@|#)+[^[a-zA-Z0-9]*]*\/+(\d+)\/+"
string = input()

matches = re.finditer(pattern, string)
for match in matches:
    print(f"You found {match.group(4)} {match.group(2)} eggs!")
