n = int(input())

for i in range(1, n + 1):
    sum = 0
    for j in str(i):
        sum += int(j)
    if sum in (5, 7, 11):
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
