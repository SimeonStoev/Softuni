from importlib.util import find_spec

numbers = input()
times = [int(number) for number in numbers.split(" ")]
first_racer_time = 0
second_racer_time = 0
winner = ""
winner_time = 0

length = len(times)

for index in range(0, int(length / 2)):
    if times[index] == 0:
        first_racer_time -= first_racer_time * 0.2
    else:
        first_racer_time += times[index]

    if times[length - 1 - index] == 0:
        second_racer_time -= second_racer_time * 0.2
    else:
        second_racer_time += times[length - 1 - index]

if first_racer_time < second_racer_time:
    winner = "left"
    winner_time = first_racer_time
else:
    winner = "right"
    winner_time = second_racer_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
