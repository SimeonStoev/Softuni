from collections import deque

number_of_stops = int(input())

queue = deque()
curr_sum = 0
curr_index = 0

for curr_stop in range(number_of_stops):
    fuel_pump_data = [int(x) for x in input().split()]
    fuel = fuel_pump_data[0]
    km_to_next_stop = fuel_pump_data[1]
    queue.append((fuel - km_to_next_stop, curr_stop))

while len(queue) > 0:
    elem = queue.popleft()
    curr_sum += elem[0]
    if curr_sum < 0:
        curr_sum = 0
        curr_index = elem[1] + 1

print(curr_index)
