from collections import deque

water_liters = int(input())
people = deque()

while True:
    person = input()
    if person == "Start":
        break

    people.append(person)

while True:
    command = input().split()

    if command[0] == "End":
        break

    if command[0] == "refill":
        water_liters += int(command[1])
