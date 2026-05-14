import math
from collections import deque

expression = input().split()
numbers = deque()

for elem in expression:
    if elem.lstrip("-").isdigit():
        numbers.append(int(elem))
    elif elem in ['+', '-', '*', '/']:
        expr = ""
        while len(numbers) > 0:
            expr += str(numbers.popleft()) + elem
        result = eval(expr[:-1])
        if elem == '/':
            result = math.floor(result)
        numbers.append(result)

result = numbers.popleft()
print(result)