list = input()
step = int(input())
players = list.split(" ")
index = 0
result = []

while len(players) > 1:
    if index + step - 1 < len(players):
        index = index + step - 1
        result.append(players[index])
        players.pop(index)
        if index == len(players):
            index = 0
    else:
        index = (index + step - 1) % len(players)
        result.append(players[index])
        players.pop(index)
        if index == len(players):
            index = 0

result.append(players[0])
players.pop(0)
print("[", end="")
for i in range(len(result)):
    if i != len(result) - 1:
        print(result[i], end=",")
    else:
        print(result[i], end="]")
