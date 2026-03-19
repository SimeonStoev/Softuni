number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    piece_data = input().split("|")
    piece = piece_data[0]
    composer = piece_data[1]
    key = piece_data[2]
    if piece not in pieces:
        pieces[piece] = {"composer": composer, "key": key}

while True:
    string = input()
    if string == "Stop":
        break

    string = string.split("|")
    command = string[0]
    if command == "Add":
        piece = string[1]
        composer = string[2]
        key = string[3]
        if piece not in pieces:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == "Remove":
        piece = string[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        piece = string[1]
        new_key = string[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in pieces.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")

