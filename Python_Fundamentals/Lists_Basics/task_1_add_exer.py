string = input()

int_array = [int(elem) for elem in string.split(", ")]
int_array_zeros = []
zero_count = 0

for elem in int_array:
    if elem != 0:
        int_array_zeros.append(elem)
    else:
        zero_count += 1

int_array_zeros.extend([0] * zero_count)

print(int_array_zeros)
