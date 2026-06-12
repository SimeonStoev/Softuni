from collections import deque

strength = [int(i) for i in input().split()]
accuracy = deque(int(i) for i in input().split())

goals_scored = 0

while len(strength) > 0 and len(accuracy) > 0:
    curr_strength = strength[-1]
    curr_accuracy = accuracy[0]

    sum = curr_strength + curr_accuracy

    if sum == 100:
        goals_scored += 1
        strength.pop()
        accuracy.popleft()
    elif sum < 100:
        if curr_strength < curr_accuracy:
            strength.pop()
        elif curr_accuracy < curr_strength:
            accuracy.popleft()
        else:
            strength[-1] = sum
            accuracy.popleft()
    else:
        strength[-1] -= 10
        accuracy.popleft()
        accuracy.append(curr_accuracy)

if goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored == 0:
    print("Paul failed to score a single goal.")
elif goals_scored > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")

if goals_scored > 0:
    print(f"Goals scored: {goals_scored}")

if len(strength) > 0:
    print(f"Strength values left: {', '.join(map(str, strength))}")

if len(accuracy) > 0:
    print(f"Accuracy values left: {', '.join(map(str, accuracy))}")
