number = int(input())
stack = []

for _ in range(number):
    command = input().split()
    if command[0] == "1":
        number_to_add = int(command[1])
        stack.append(number_to_add)
    elif len(stack) > 0:
        if command[0] == "2" and len(stack) > 0:
            stack.pop()
        elif command[0] == "3":
            print(max(stack))
        elif command[0] == "4":
            print(min(stack))

result = ""
while len(stack) > 0:
    result += str(stack.pop())
    if len(stack) > 0:
        result += ", "

print(result)
