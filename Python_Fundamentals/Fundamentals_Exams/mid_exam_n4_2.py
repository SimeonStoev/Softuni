products = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split(" ")
    if command[0] == "Urgent" and command[1] not in products:
        products.insert(0, command[1])
    elif command[0] == "Unnecessary" and command[1] in products:
        products.remove(command[1])
    elif command[0] == "Correct" and command[1] in products:
        products[products.index(command[1])] = command[2]
    elif command[0] == "Rearrange" and command[1] in products:
        products.remove(command[1])
        products.append(command[1])
    command = input()

result = ", ".join(map(str, products))
print(result)
