ints = input().split()

stack = []

for integer in ints:
    stack.append(int(integer))

while len(stack) > 0:
    print(stack.pop(), end=" ")
