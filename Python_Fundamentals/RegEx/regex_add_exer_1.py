import re

participants = input().split(", ")

tour_info = {}

while True:
    string = input()
    if string == "end of race":
        break
    clear_pattern_for_name = r"\W+|\d+"
    clear_pattern_for_numbers = r"\D+"
    name = re.sub(clear_pattern_for_name, "", string)
    if name in participants:
        distance = sum([int(digit) for digit in re.sub(clear_pattern_for_numbers, "", string)])
        if name in tour_info.keys():
            tour_info[name] += distance
        else:
            tour_info[name] = distance

# tour_info_sorted = sorted(tour_info.items(), key=lambda x: x[1], reverse=True)

participants_sorted = [part_name for part_name, distance in sorted(tour_info.items(), key=lambda item:item[1], reverse=True)]

print(f"1st place: {participants_sorted[0]}")
print(f"2nd place: {participants_sorted[1]}")
print(f"3rd place: {participants_sorted[2]}")