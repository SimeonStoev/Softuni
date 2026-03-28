import re
import math

string = input()

pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
pattern_numbers = r"\d"

cool_threshold = math.prod([int(number) for number in re.findall(pattern_numbers, string)])
cool_emojis = []
emojis_count = 0

matches = re.finditer(pattern, string)
for match in matches:
    emojis_count += 1
    emoji = match.group()
    emoji = emoji[2:len(emoji) - 2]
    emoji_len = sum([ord(elem) for elem in emoji])
    if emoji_len >= cool_threshold:
        cool_emojis.append(match.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
