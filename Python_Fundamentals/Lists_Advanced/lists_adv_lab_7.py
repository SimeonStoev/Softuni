employees_happy = [int(x) for x in input().split()]
factor = int(input())

employees_mulp_by_factor = list(map(lambda x: x * factor, employees_happy))
average = sum(employees_mulp_by_factor) / len(employees_happy)

employees_happy_above_average = len(list(filter(lambda x: x >= average, employees_mulp_by_factor)))

if employees_happy_above_average >= len(employees_happy) / 2:
    print(f"Score: {employees_happy_above_average}/{len(employees_happy)}. Employees are happy!")
else:
    print(f"Score: {employees_happy_above_average}/{len(employees_happy)}. Employees are not happy!")
