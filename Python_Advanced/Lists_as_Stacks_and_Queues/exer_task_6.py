expression = input()

parantheses = []
invalid_expression = False

for char in expression:
    if char in ('{', '[', '('):
        parantheses.append(char)
    else:
        if len(parantheses) == 0 or (ord(parantheses[-1]) + 2 != ord(char) and char in ('}', ']')) or (
                ord(parantheses[-1]) + 1 != ord(char) and char == ')'):
            invalid_expression = True
            break

        parantheses.pop()

if invalid_expression:
    print("NO")
else:
    print("YES")
