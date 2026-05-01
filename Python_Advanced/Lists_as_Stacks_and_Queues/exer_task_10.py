"""
Cup and Bottle Water Filling Simulation

This program simulates filling cups with water from bottles.
Cups are processed in order (queue), and bottles are used from the end (stack).
Water is poured from each bottle into the current cup until the cup is full or the bottle is empty.
Excess water from the bottle is wasted if the cup is filled.
The simulation continues until either all cups are filled or all bottles are used.
Finally, it reports remaining cups or bottles and the total wasted water.
"""

from collections import deque

# Read input: cups capacities (space-separated integers)
cups = deque([int(x) for x in input().split()])
# Read input: bottles capacities (space-separated integers, used as stack)
bottles = [int(x) for x in input().split()]
# Initialize wasted water counter
wasted_water = 0

# Main simulation loop: continue while there are cups and bottles
while len(cups) > 0 and len(bottles) > 0:
    bottle = bottles.pop()  # Get the last bottle (stack behavior)
    cup = cups[0]  # Peek at the first cup (queue behavior)
    cup -= bottle  # Subtract bottle capacity from cup capacity

    # If cup is filled or overfilled
    if cup <= 0:
        cups.popleft()  # Remove the filled cup
        wasted_water += abs(cup)  # Add excess water to wasted (if cup < 0)
    else:
        cups[0] = cup  # Update the cup's remaining capacity

# Output results based on what remains
if len(bottles) == 0:  # No bottles left, some cups may remain
    print(f"Cups: {' '.join(map(str, cups))}")
else:  # No cups left, some bottles may remain
    print(f"Bottles: {' '.join(map(str, bottles))}")

# Print total wasted water
print(f"Wasted litters of water: {wasted_water}")
