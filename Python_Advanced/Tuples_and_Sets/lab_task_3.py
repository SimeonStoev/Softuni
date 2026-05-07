# This script reads a specified number of elements from input, stores them in a set
# to automatically handle uniqueness, and then prints each unique element on a new line.

# Read the number of elements to process
number_of_elems = int(input())

# Initialize an empty set to store unique elements
unique_elements = set()

# Loop for the number of elements
for _ in range(number_of_elems):
    # Read each element from input
    element = input()
    # Add the element to the set (duplicates are automatically ignored)
    unique_elements.add(element)

# Print all unique elements, each on a new line
print("\n".join(unique_elements))
