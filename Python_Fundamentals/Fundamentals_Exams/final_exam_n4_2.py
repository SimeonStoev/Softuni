import re

pattern = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"

n = int(input())

for _ in range(n):
    barcode = input()
    match = re.search(pattern, barcode)
    if match:
        barcode_inside = match.group(2)
        product_group = "".join(re.findall(r"[0-9]+", barcode_inside))
        if len(product_group) == 0:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
