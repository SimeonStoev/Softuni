import re


# ^%[A-Z][a-z]+%[^|$%.]*<\w+>[^|$%.]*\|([0]|[1-9][0-9]*)\|[^|$%.]*(?<!0)(0|[1-9]+)(\.[0-9]+)?\$$

def is_valid(pat, string):
    return bool(re.search(pat, string))


pattern = r"%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|([0]|[1-9][0-9]*)\|[^|$%.]*((?<!\d)(0|[1-9][0-9]*)(\.[0-9]+)?)\$$"
total_income = 0

while True:
    input_string = input()
    if input_string == "end of shift":
        break

    if is_valid(pattern, input_string):
        name = re.search(pattern, input_string).group(1)
        product = re.search(pattern, input_string).group(2)
        count = int(re.search(pattern, input_string).group(3))
        price = float(re.search(pattern, input_string).group(4))
        total_income += count * price
        print(f"{name}: {product} - {count * price:.2f}")

print(f"Total income: {total_income:.2f}")
