command = ""
metres_for_day = 0
height_level_reached = 5364
days = 1

while command != "END" and height_level_reached < 8848 and days <= 5:
    command = input()
    if command != "END":
        if command == "Yes":
            days += 1
        if days <= 5:
            metres_for_day = int(input())
            height_level_reached += metres_for_day

if height_level_reached >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{height_level_reached}")