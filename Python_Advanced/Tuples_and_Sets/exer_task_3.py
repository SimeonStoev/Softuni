# This script reads a specified number of lines, splits each line into space-separated elements,
# collects all unique elements into a set, and prints them, each on a new line.

# Read the number of lines to process
number_of_elems = int(input())

# Initialize an empty set to store all unique elements
chem_elems = set()

# Loop for the number of lines
for _ in range(number_of_elems):
    # Read a line, split it into space-separated parts, and add all parts to the set
    # The update() method adds multiple elements from the iterable to the set
    chem_elems.update(input().split())

# Print all unique elements, each on a new line
print("\n".join(chem_elems))
