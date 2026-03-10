key = [int(elem) for elem in input().split()]
key_len = len(key)

while True:
    string = input()

    if string == "find":
        break
    decrypted_string = ""
    for index in range(len(string)):
        key_index = -1
        if index < key_len:
            key_index = index
        else:
            key_index = index % key_len

        decrypted_string += chr(ord(string[index]) - key[key_index])

    first_index_for_treasure = decrypted_string.find("&")
    second_index_for_treasure = decrypted_string.find("&", first_index_for_treasure + 1)

    treasure = decrypted_string[first_index_for_treasure + 1:second_index_for_treasure]
    coordinates = decrypted_string[decrypted_string.find("<") + 1:decrypted_string.find(">")]
    
    print(f"Found {treasure} at {coordinates}")
