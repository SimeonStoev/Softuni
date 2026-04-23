from collections import deque

people = deque()

while True:
    name = input()

    if name == "End":
        break

    if name == "Paid":
        for _ in range(len(people)):
            person = people.popleft()
            print(person)
    else:
        people.append(name)

print(f"{len(people)} people remaining.")
