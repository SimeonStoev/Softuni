# This script reads two integers representing the sizes of two sets,
# populates each set with that many elements, finds their intersection,
# and prints the common elements.

# Read two integers n and m from input, where n is the size of set_1 and m is the size of set_2
n, m = [int(x) for x in input().split()]

# Initialize two empty sets
set_1 = set()
set_2 = set()

# Loop n times to read and add elements to the first set
for _ in range(n):
    set_1.add(input())

# Loop m times to read and add elements to the second set
for _ in range(m):
    set_2.add(input())

# Compute the intersection of both sets (elements present in both sets)
intersection_set = set_1 & set_2

# Print all common elements, each on a new line
print("\n".join(intersection_set))
