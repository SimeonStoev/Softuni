sequence1 = set(map(int, input().split()))
sequence2 = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            sequence1.update(map(int, command[2:]))
        elif command[1] == 'Second':
            sequence2.update(map(int, command[2:]))
    elif command[0] == 'Remove':
        if command[1] == 'First':
            sequence1.difference_update(map(int, command[2:]))
        elif command[1] == 'Second':
            sequence2.difference_update(map(int, command[2:]))
    elif command[0] == 'Check':
        if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
            print('True')
        else:
            print('False')

print(f'{", ".join(map(str, sorted(sequence1)))}')
print(f'{", ".join(map(str, sorted(sequence2)))}')