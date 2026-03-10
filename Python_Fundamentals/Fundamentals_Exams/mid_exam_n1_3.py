sequence = input().split(" ")
moves = 0

command = input()

while command != "end":
    moves += 1
    command = command.split(" ")
    first_index = int(command[0])
    second_index = int(command[1])

    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(
            sequence) or second_index >= len(sequence):
        print("Invalid input! Adding additional elements to the board")
        mid_elem_pos = int(len(sequence) / 2)
        sequence.insert(mid_elem_pos, "-" + str(moves) + "a")
        sequence.insert(mid_elem_pos + 1, "-" + str(moves) + "a")
    elif sequence[first_index] == sequence[second_index]:
        elem_to_remove = sequence[first_index]
        print(f"Congrats! You have found matching elements - {elem_to_remove}!")
        sequence.remove(elem_to_remove)
        sequence.remove(elem_to_remove)
    else:
        print("Try again!")

    if len(sequence) == 0:
        break

    command = input()

if command != "end":
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    for elem in sequence:
        print(f"{elem}", end=" ")
