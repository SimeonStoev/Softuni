import re

pattern = r"(=|\/)[A-Z][a-zA-Z][a-zA-Z]+\1"

input = input()
destinations= []
travel_points = 0

matches = re.finditer(pattern, input)
for match in matches:
    destination = match.group()
    len_dest = len(destination)
    destinations.append(destination[1:len_dest-1])
    travel_points += len_dest - 2

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")