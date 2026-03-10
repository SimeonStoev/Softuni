distance_to_pokomen = list(map(int, input().split(" ")))
removed_element = 0
sum = 0

while len(distance_to_pokomen) > 0:
    index = int(input())
    if index < 0:
        removed_element = distance_to_pokomen[0]
        distance_to_pokomen[0] = distance_to_pokomen[len(distance_to_pokomen) - 1]
    elif index >= len(distance_to_pokomen):
        removed_element = distance_to_pokomen[len(distance_to_pokomen) - 1]
        distance_to_pokomen[len(distance_to_pokomen) - 1] = distance_to_pokomen[0]
    else:
        removed_element = distance_to_pokomen[index]
        distance_to_pokomen.pop(index)

    for i in range(len(distance_to_pokomen)):
        if distance_to_pokomen[i] <= removed_element:
            distance_to_pokomen[i] += removed_element
        else:
            distance_to_pokomen[i] -= removed_element

    sum += removed_element

print(sum)
