import math
from collections import deque

bees = deque(int(i) for i in input().split())
bee_eaters = [int(i) for i in input().split()]

while len(bees) > 0 and len(bee_eaters) > 0:
    bee_group = bees.popleft()
    bee_eater_group = bee_eaters[-1]

    if bee_eater_group * 7 >= bee_group:
        if bee_eater_group * 7 == bee_group:
            bee_eaters.pop()
        else:
            survived_bee_eaters = math.ceil(((bee_eater_group * 7) - bee_group) / 7)
            bee_eaters[-1] = survived_bee_eaters
    else:
        survived_bees = bee_group - (bee_eater_group * 7)
        bees.append(survived_bees)
        bee_eaters.pop()

print("The final battle is over!")

if len(bee_eaters) == 0 and len(bees) == 0:
    print("But no one made it out alive!")
elif len(bees) > 0:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif len(bee_eaters) > 0:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")
