import re

sequence_of_chars = input()

all_names = re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', sequence_of_chars)

print(" ".join(all_names))