expression = input()

stack_indexes = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack_indexes.append(index)
    if expression[index] == ")":
        start_index = stack_indexes.pop()
        end_index = index
        print(expression[start_index:end_index+1])