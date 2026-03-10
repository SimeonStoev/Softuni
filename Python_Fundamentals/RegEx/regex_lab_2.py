import re

string_with_phone_numbers = input()

# phone_numbers = re.finditer(r'(?<!\S)\+359(?:\s|-)2(?:\s|-)(\d{3})(?:\s|-)(\d{4})', string_with_phone_numbers)
# phone_numbers = re.findall(r'(?<!\S)\+359(?:\s|-)2(?:\s|-)\d{3}(?:\s|-)\d{4}', string_with_phone_numbers)
phone_numbers = re.findall(r'(?<!\S)\+359(?:\s2\s\d{3}\s\d{4}\b|-2-\d{3}-\d{4}\b)', string_with_phone_numbers)
print(", ".join(phone_numbers))

#for phone_number in phone_numbers:
#    print(phone_number)