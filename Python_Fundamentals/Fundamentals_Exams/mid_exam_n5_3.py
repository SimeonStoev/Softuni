items = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    command_test = command[0]
    command_item = command[1]
    if command[0] == "Collect":
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        combine_items = command[1].split(":")
        if combine_items[0] in items:
            index = items.index(combine_items[0])
            items.insert(index + 1, combine_items[1])
    elif command[0] == "Renew":
        if command[1] in items:
            item = command[1]
            items.remove(item)
            items.append(item)
    command = input()

print(", ".join(map(str, items)))
