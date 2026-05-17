from collections import deque


def are_presents_crafted(p_crafted_presents):
    return ("Doll" in p_crafted_presents and "Wooden train" in p_crafted_presents) or (
            "Teddy bear" in p_crafted_presents and "Bicycle" in p_crafted_presents)


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_presents = {}

while len(magic_levels) > 0 and len(materials) > 0:
    material = materials[-1]
    magic_level = magic_levels[0]
    product = material * magic_level

    if product in presents:
        materials.pop()
        magic_levels.popleft()

        if presents[product] not in crafted_presents:
            crafted_presents[presents[product]] = 0
        crafted_presents[presents[product]] += 1
    elif product < 0:
        sum_of_values = material + magic_level
        materials.pop()
        magic_levels.popleft()
        materials.append(sum_of_values)
    elif product > 0:
        magic_levels.popleft()
        materials[-1] += 15
    else:
        if material == 0:
            materials.pop()
        if magic_level == 0:
            magic_levels.popleft()

if are_presents_crafted(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials) > 0:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")

if len(magic_levels) > 0:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for toy_name in sorted(crafted_presents.keys()):
    print(f"{toy_name}: {crafted_presents[toy_name]}")
