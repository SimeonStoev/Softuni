year = int(input())
happy_year_found = False
next_year = year + 1
year_numbers = []
year_numbers.extend(str(next_year))

while not happy_year_found:
    if len(year_numbers) == len(set(year_numbers)):
        happy_year_found = True
    else:
        year_numbers.clear()
        next_year += 1
        year_numbers.extend(str(next_year))

print(next_year)