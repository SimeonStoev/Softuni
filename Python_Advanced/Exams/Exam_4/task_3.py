def accommodate(*args, **kwargs):
    guest_groups = list(args)
    rooms = dict(sorted(kwargs.items(), key=lambda x: (x[1], int(x[0][-3:]))))
    accommodate_rooms = {}
    unaccommodate_guests = 0
    for guest_count in guest_groups:
        found_room = False
        for room, room_capacity in rooms.items():
            if guest_count <= room_capacity:
                found_room = True
                rooms.pop(room)
                accommodate_rooms[room] = guest_count
                break
        if not found_room:
            unaccommodate_guests += guest_count

    accommodate_rooms = dict(sorted(accommodate_rooms.items(), key=lambda x: int(x[0][-3:])))

    result = ""
    if len(accommodate_rooms) > 0:
        result += f"A total of {len(accommodate_rooms)} accommodations were completed!\n"
        for room, guests in accommodate_rooms.items():
            result += f"<Room {room[-3:]} accommodates {guests} guests>\n"
    else:
        result += "No accommodations were completed!\n"

    if unaccommodate_guests > 0:
        result += f"Guests with no accommodation: {unaccommodate_guests}\n"

    empty_rooms = len(kwargs) - len(accommodate_rooms)
    if empty_rooms > 0:
        result += f"Empty rooms: {empty_rooms}"

    return result


print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
