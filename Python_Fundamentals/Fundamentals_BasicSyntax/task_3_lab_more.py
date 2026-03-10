queue_of_sheeps = input()
list_of_sheeps = queue_of_sheeps.split(", ")
list_of_sheeps_len = len(list_of_sheeps)

position_of_wolf = list_of_sheeps.index("wolf")

if position_of_wolf == list_of_sheeps_len - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {list_of_sheeps_len - position_of_wolf - 1}! You are about to be eaten by a wolf!")
