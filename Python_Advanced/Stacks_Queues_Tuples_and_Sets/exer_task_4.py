from collections import deque

bees = deque([int(bee) for bee in input().split()])
nectars = [int(n) for n in input().split()]
symbols = deque(input().split())
honey = 0

while len(bees) != 0 and len(nectars) != 0:
    bee = bees.popleft()
    nectar = nectars.pop()

    while nectar < bee and len(nectars) > 0:
        nectar = nectars.pop()

    if nectar >= bee:
        symbol = symbols.popleft()
        expression = str(bee) + symbol + str(nectar)
        if symbol == "/" and nectar == 0:
            continue
        honey += abs(eval(expression))
    else:
        bees.appendleft(bee)

print(f"Total honey made: {honey}")
if len(bees) > 0:
    print(f"Bees left: {', '.join(map(str, bees))}")
if len(nectars) > 0:
    print(f"Nectar left: {', '.join(map(str, nectars))}")
