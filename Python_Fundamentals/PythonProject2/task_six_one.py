a1 = int(input())
a2 = int(input())
n = int(input())

for i in range(a1, a2):
    ascii_symbol = chr(i)
    for j in range(1, n):
        for k in range(1, int(n / 2)):
            if i % 2 != 0 and (j + k + i) % 2 != 0:
                print(f"{ascii_symbol}-{j}{k}{i}")
