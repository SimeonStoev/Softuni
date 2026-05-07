# This script processes n names, calculates a modified ASCII sum for each (sum of ASCII values divided by position),
# classifies these sums as even or odd, and prints a result based on the comparison of the sum totals.

# Read the number of names to process
n = int(input())

# Initialize a set to store even ASCII sums
even_set = set()

# Initialize a set to store odd ASCII sums
odd_set = set()

# Loop through each name with position counter starting from 1
for i in range(1, n + 1):
    # Read a name
    name = input()

    # Calculate the sum of ASCII values of all characters in the name, divided by the position
    ascii_sum = sum([ord(char) for char in name]) // i

    # Check if the result is even
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    # Otherwise, the result is odd
    else:
        odd_set.add(ascii_sum)

# Calculate the sum of all elements in the odd set
odd_set_sum = sum(odd_set)

# Calculate the sum of all elements in the even set
even_set_sum = sum(even_set)

# If the sums are equal, print the union of both sets
if odd_set_sum == even_set_sum:
    print(f"{', '.join(map(str, list(odd_set | even_set)))}")
# If odd sum is greater, print elements in odd set but not in even set
elif odd_set_sum > even_set_sum:
    print(f"{', '.join(map(str, list(odd_set - even_set)))}")
# Otherwise, print the symmetric difference (elements in either set but not in both)
else:
    print(f"{', '.join(map(str, list(odd_set ^ even_set)))}")
