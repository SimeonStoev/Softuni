# This script manages a guest list by first adding a specified number of guests,
# then removing guests based on subsequent inputs until "END" is entered.
# Finally, it prints the number of remaining guests and their names in sorted order.

# Read the initial number of guests
number_of_guests = int(input())

# Initialize an empty set to store guest names (ensures uniqueness)
list_of_guests = set()

# Loop to add each initial guest
for _ in range(number_of_guests):
    list_of_guests.add(input())

# Loop to process guest removals until "END" is entered
while True:
    # Read the next guest name or "END"
    guest = input()
    # If "END" is entered, break the loop
    if guest in "END":
        break
    # Otherwise, remove the guest from the set (assuming they exist)
    list_of_guests.remove(guest)

# Convert the set to a sorted list of remaining guests
list_of_guests_left = sorted(list(list_of_guests))

# Print the number of remaining guests
print(len(list_of_guests_left))

# Print each remaining guest on a new line
print("\n".join(list_of_guests_left))
