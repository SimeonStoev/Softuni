names = input().split(", ")
names.sort(key=lambda name: (-len(name), name))
print(names)
