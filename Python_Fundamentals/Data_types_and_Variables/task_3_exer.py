number_of_people = int(input())
capacity = int(input())

elevator_courses = 0

if number_of_people % capacity == 0:
    elevator_courses = number_of_people // capacity
else:
    elevator_courses = (number_of_people // capacity) + 1

print(elevator_courses)