number = int(input())
is_prime = True

for i in range(2, number - 1):
    if not is_prime:
        break
    for j in range(i + 1, number):
        if i * j == number:
            is_prime = False

print(is_prime)
