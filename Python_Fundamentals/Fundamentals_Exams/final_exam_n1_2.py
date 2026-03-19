import re

patter = r"(\||#)[a-zA-Z\s]+\1\d{2}\/\d{2}\/\d{2}\1(?:[0-9]{1,4}|10000)\1"

string = input()

matches = re.finditer(patter, string)

total_kcal = 0
food_data_matrix = []

for match in matches:
    delimiter = match.group()[0]
    food_data = [elem for elem in match.group().split(delimiter) if elem != ""]
    total_kcal += int(food_data[2])
    food_data_matrix.append(food_data)


total_days = total_kcal // 2000

print(f"You have food to last you for: {total_days} days!")

for food in food_data_matrix:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")