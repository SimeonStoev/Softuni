import re


def get_demon_health(name):
    result = 0
    pattern = r"[^0-9+\/*-.]+"
    match = "".join(re.findall(pattern, name))
    for char in match:
        result += ord(char)

    return result


def get_demon_damage(name):
    result = 0
    pattern = r"[+-]?\d+(\.\d+)?"  # r"([+-])?[0-9]+(\.[0-9]+)*"  # integer or floating point number pattern
    add_pattern = r"[\/*]+"
    matches = re.finditer(pattern, name)
    for match in matches:
        result += float(match.group())

    add_actions = "".join(re.findall(add_pattern, name))
    for action in add_actions:
        if action == "*":
            result *= 2
        else:
            result /= 2

    return result


demons_names = "".join(input().split(",")).split()

demons = {}

for demon in demons_names:
    if len(demon) > 0:
        demon_health = get_demon_health(demon)
        demon_damage = get_demon_damage(demon)
        demons[demon] = (demon_health, demon_damage)

sorted_demons = {key: value for key, value in sorted(demons.items(), key=lambda item: item[0])}
for demon in sorted_demons.keys():
    print(f"{demon} - {sorted_demons[demon][0]} health, {sorted_demons[demon][1]:.2f} damage")
