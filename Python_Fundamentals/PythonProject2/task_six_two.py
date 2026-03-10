number = int(input())
baker_name_winner = ""
baker_points_winner = 0

for i in range(1, number + 1):
    name = input()
    points = 0
    command = ""

    while command != "Stop":
        command = input()
        if command != "Stop":
            points += int(command)

    print(f"{name} has {points} points.")
    
    if points > baker_points_winner:
        baker_name_winner = name
        baker_points_winner = points
        print(f"{baker_name_winner} is the new number 1!")

print(f"{baker_name_winner} won competition with {baker_points_winner} points!")
