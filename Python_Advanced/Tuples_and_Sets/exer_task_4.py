# This script reads a text input, converts it to a tuple of characters,
# and prints each unique character in sorted order along with its count of occurrences.

# Read the input text
text = input()

# Convert the text string into a tuple of individual characters
tuple_chars = tuple(text)

# Initialize an empty list to track characters that have already been printed
visited_chars = []

# Loop through each character in the sorted tuple of characters
for char in sorted(tuple_chars):
    # Check if the character has not been printed yet
    if char not in visited_chars:
        # Print the character and its count in the original tuple
        print(f"{char}: {tuple_chars.count(char)} time/s")
        # Add the character to the visited list
        visited_chars.append(char)
