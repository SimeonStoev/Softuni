number_of_rooms = int(input())
room_number = 1
all_chairs = 0
all_people = 0

while room_number <= number_of_rooms:
    room_data = input().split(" ")
    number_of_chairs = len(room_data[0])
    number_of_people = int(room_data[1])
    all_chairs += number_of_chairs
    all_people += number_of_people

    if number_of_chairs < number_of_people:
        print(f"{number_of_people - number_of_chairs} more chairs needed in room {room_number}")
    room_number += 1

if all_chairs > all_people:
    print(f"Game On, {all_chairs - all_people} free chairs left")
