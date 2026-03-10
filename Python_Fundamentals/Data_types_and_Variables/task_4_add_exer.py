lines = int(input())
brackets = []
result = "BALANCED"
for i in range(1, lines + 1):
    string = input()
    if string in ('(', ')'):
        brackets.append(string)

if len(brackets) % 2 != 0:
    result = "UNBALANCED"
else:
    for i in range(len(brackets)):
        if i % 2 == 0:
            if brackets[i] != '(':
                result = "UNBALANCED"
        else:
            if brackets[i] != ')':
                result = "UNBALANCED"

print(result)
