from collections import deque

kids = input().split()
curr_pos = 1
toss = int(input())

kids_queue = deque()

while len(kids) > 0:
    if curr_pos + toss - 1 > len(kids):
        curr_pos = ((curr_pos + toss - 1) % len(kids))
        if curr_pos == 0:
            curr_pos = len(kids)
    else:
        curr_pos += toss - 1

    kid = kids.pop(curr_pos - 1)
    if curr_pos > len(kids):
        curr_pos = 1

    kids_queue.append(kid)

while len(kids_queue) > 0:
    kid = kids_queue.popleft()
    if len(kids_queue) == 0:
        print(f"Last is {kid}")
    else:
        print(f"Removed {kid}")
