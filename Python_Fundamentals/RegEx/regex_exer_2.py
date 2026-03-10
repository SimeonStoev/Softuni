import re

pattern = r"(?<!\w)_([A-Za-z0-9]+)(?!\w)"

text = input()

matches = re.findall(pattern, text)
print(",".join(matches))