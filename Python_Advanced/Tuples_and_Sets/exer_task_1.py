# This script reads a specified number of names from input, stores them in a set
# to automatically remove duplicates, and prints each unique name on a new line.

# Read the number of names to process
n = int(input())

# Initialize an empty set to store unique names
names_unique = set()

# Loop for the number of names
for _ in range(n):
    # Read a name from input
    name = input()
    # Add the name to the set (duplicates are automatically ignored)
    names_unique.add(name)

# Print all unique names, each on a new line
print("\n".join(names_unique))
