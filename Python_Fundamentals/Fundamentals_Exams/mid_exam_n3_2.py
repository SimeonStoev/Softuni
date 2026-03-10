targets = [int(x) for x in input().split(" ")]
index = input()
number_of_targets = len(targets)

while index != "End":
    index = int(index)
    if 0 <= index < number_of_targets and targets[index] != -1:
        for i in range(number_of_targets):
            if i != index and targets[i] != -1:
                if targets[i] > targets[index]:
                    targets[i] -= targets[index]
                else:
                    targets[i] += targets[index]

        targets[index] = -1

    index = input()

shot_targets = targets.count(-1)
targets_str = " ".join(map(str, targets))

print(f"Shot targets: {shot_targets} -> {targets_str}")
