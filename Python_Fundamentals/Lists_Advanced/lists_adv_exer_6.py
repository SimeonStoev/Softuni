import math

number_of_electrons = int(input())
shells = []
counter = 1

while number_of_electrons > 0:
    electrons_for_shell = 2 * math.pow(counter, 2)
    if electrons_for_shell <= number_of_electrons:
        shells.append(int(electrons_for_shell))
        number_of_electrons -= electrons_for_shell
    else:
        shells.append(int(number_of_electrons))
        number_of_electrons = 0
    counter += 1

print(shells)
