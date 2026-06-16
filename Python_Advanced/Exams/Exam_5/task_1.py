from collections import deque

contestants = deque([int(i) for i in input().split()])
pies = [int(i) for i in input().split()]

while len(contestants) > 0 and len(pies) > 0:
    contest_group = contestants.popleft()
    pie = pies[0]

    if contest_group >= pie:
        pies.pop(0)
        if contest_group - pie > 0:
            contestants.append(contest_group - pie)
    else:
        pie -= contest_group
        if pie == 1 and len(pies) > 1:
            pies.pop(0)
            pies[0] += pie
        else:
            pies[0] = pie

if len(pies) == 0 and len(contestants) > 0:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")
elif len(pies) > 0 and len(contestants) == 0:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")
else:
    print("We have a champion!")
