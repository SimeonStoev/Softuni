number_of_guests = int(input())
list_of_guests = set()

for _ in range(number_of_guests):
    list_of_guests.add(input())

while True:
    guest = input()
    if guest in "END":
        break

    list_of_guests.remove(guest)

list_of_guests_left = sorted(list(list_of_guests))
print(len(list_of_guests_left))
print("\n".join(list_of_guests_left))
