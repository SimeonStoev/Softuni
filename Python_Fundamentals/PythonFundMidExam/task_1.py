energy = float(input())
terrain = input()
artefacts_found = 0
curr_mountain_terrain = 0

while terrain != "Journey ends here!" and energy > 0 and artefacts_found < 3:
    if terrain == "mountain":
        energy -= 10
        curr_mountain_terrain += 1
        if curr_mountain_terrain % 3 == 0:
            artefacts_found += 1
    elif terrain == "desert":
        energy -= 15
    elif terrain == "forest":
        energy += 7

    terrain = input()

if artefacts_found == 3:
    print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
elif energy <= 0:
    print("The character is too exhausted to carry on with the journey.")
else:
    print(
        f"The character could not find all the pieces and needs {3 - artefacts_found} more to complete the legendary artifact.")
