from collections import deque

worms = [int(i) for i in input().split()]
worms_count = len(worms)
holes = deque([int(i) for i in input().split()])
match_count = 0

while len(worms) > 0 and len(holes) > 0:
    worm = worms[-1]
    hole = holes.popleft()

    if worm == hole:
        worms.pop()
        match_count += 1
    else:
        worm -= 3
        if worm <= 0:
            worms.pop()
        else:
            worms[-1] = worm

if match_count > 0:
    print(f"Matches: {match_count}")
else:
    print("There are no matches.")

if len(worms) == 0 and match_count == worms_count:
    print("Every worm found a suitable hole!")
elif len(worms) == 0 and match_count < worms_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worms))}")

if len(holes) == 0:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
