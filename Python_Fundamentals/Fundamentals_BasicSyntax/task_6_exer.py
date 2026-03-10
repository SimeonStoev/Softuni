n = int(input())

for i in range(n):
    string = input()
    if string.find(',') != -1 or string.find('.') != -1 or string.find('_') != -1:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")