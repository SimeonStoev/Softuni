# This script reads multiple pairs of numeric ranges, finds the intersection of each pair,
# and prints the longest intersection along with its length.

# Read the number of range pairs to process
n = int(input())

# Initialize an empty list to store the intersections of all range pairs
sets_list = []

# Loop for each range pair
for _ in range(n):
    # Read a line and split it by '-' to separate the two ranges
    ranges = input().split('-')

    # Parse the first range: split by comma and convert to integers
    first_range = [int(x) for x in ranges[0].split(",")]

    # Parse the second range: split by comma and convert to integers
    second_range = [int(x) for x in ranges[1].split(",")]

    # Create a set from the first range (inclusive on both ends)
    set_1 = set(list(range(first_range[0], first_range[1] + 1)))

    # Create a set from the second range (inclusive on both ends)
    set_2 = set(list(range(second_range[0], second_range[1] + 1)))

    # Find the intersection of both sets and add it to the list
    sets_list.append(set_1 & set_2)

# Sort the list of intersections by their length in descending order
sorted_sets_list = sorted(sets_list, key=lambda x: len(x), reverse=True)

# Print the longest intersection with its elements and length
print(f"Longest intersection is [{', '.join(map(str, sorted_sets_list[0]))}] with length {len(sorted_sets_list[0])}")
