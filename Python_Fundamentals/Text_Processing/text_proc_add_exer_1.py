lines = int(input())

for _ in range(lines):
    string = input()
    name = string[string.find("@") + 1:string.find("|")]
    age = string[string.find("#") + 1:string.find("*")]
    print(f"{name} is {age} years old.")
