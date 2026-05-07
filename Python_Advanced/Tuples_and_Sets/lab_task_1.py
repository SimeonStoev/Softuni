# This script reads a line of input, splits it into numbers, converts them to floats,
# and stores them in a tuple. It then iterates through the tuple, tracking unique numbers
# and printing each unique number along with its count of occurrences.

# Read input from user, split into list of strings, convert each to float, and create a tuple
numbers = tuple([float(x) for x in input().split()])

# Initialize an empty list to keep track of numbers that have already been printed
printed_numbers = []

# Loop through each number in the tuple
for number in numbers:
    # Check if the number has not been printed yet
    if number not in printed_numbers:
        # Add the number to the list of printed numbers
        printed_numbers.append(number)
        # Print the number formatted to one decimal place, followed by its count in the tuple
        print(f"{number:.1f} - {numbers.count(number)} times")
