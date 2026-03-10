import re

string = input()
word = input()

pattern = f"\\b{word}\\b"
matches = re.findall(pattern, string, flags=re.IGNORECASE)
print (len(matches))