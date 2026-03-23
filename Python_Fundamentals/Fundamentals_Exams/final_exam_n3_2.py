import re

pattern = r"(@|#)([a-zA-Z][a-zA-Z][a-zA-Z]+)\1\1([a-zA-Z][a-zA-Z][a-zA-Z]+)\1"

text = input()

words_found = 0
mirror_words_found = 0
mirror_words = []

matches = re.finditer(pattern, text)
for match in matches:
    first_word = match.group(2)
    second_word = match.group(3)
    if first_word == second_word[::-1]:
        mirror_words_found += 1
        mirror_words.append(first_word + " <=> " + second_word)
    words_found += 1

if words_found == 0:
    print(f"No word pairs found!")
else:
    print(f"{words_found} word pairs found!")

if mirror_words_found == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))