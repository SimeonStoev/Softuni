import re

# >>sofa<<10.5!5

pattern = r"^>>(\w+)<<((?:[0]|[1-9][0-9]*)(?:\.\d+)?)!([0]|[1-9][0-9]*)(?!\d+)"
furnitures = []
total_sum = 0

while True:
    string = input()

    if string == "Purchase":
        break

    matches = re.finditer(pattern, string)

    for match in matches:
        furnitures.append(match.group(1))
        total_sum += float(match.group(2)) * float(match.group(3))


if len(furnitures) > 0:
    print("Bought furniture:")
    print("\n".join(furnitures))
    print(f"Total money spend: {total_sum:.2f}")