songs = input().split()
number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split(" * ")
    if command[0] == "Add Song":
        song = command[1]
        if song not in songs:
            songs.append(song)
            print(f"{song} successfully added")
    elif command[0] == "Delete Song":
        number_of_songs_to_del = int(command[1])
        if len(songs) >= number_of_songs_to_del:
            deleted_songs = ", ".join(songs[:number_of_songs_to_del])
            songs = songs[number_of_songs_to_del:]
            print(f"{deleted_songs} deleted")
    elif command[0] == "Shuffle Songs":
        song_index1 = int(command[1])
        song_index2 = int(command[2])
        if 0 <= song_index1 < len(songs) and 0 <= song_index2 < len(songs):
            songs[song_index1], songs[song_index2] = songs[song_index2], songs[song_index1]
            print(f"{songs[song_index1]} is swapped with {songs[song_index2]}")
    elif command[0] == "Insert":
        song = command[1]
        index = int(command[2])
        if 0 <= index < len(songs):
            if song not in songs:
                songs.insert(index, song)
                print(f"{song} successfully inserted")
            else:
                print("Song is already in the playlist")
        else:
            print("Index out of range")
    elif command[0] == "Sort":
        songs.sort(reverse=True)
    elif command[0] == "Play":
        print("Songs to Play:")
        for song in songs:
            print(song)
