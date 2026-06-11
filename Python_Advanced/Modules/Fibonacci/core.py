fibonacci_seq = []

def reset_fibonacci_seq():
    fibonacci_seq.clear()

def create_fibonacci_seq(n):
    global fibonacci_seq
    reset_fibonacci_seq()
    if n == 1:
        fibonacci_seq.append(0)
    else:
        fibonacci_seq.extend([0, 1])
        for i in range(2, n):
            fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])

    print(*fibonacci_seq)

def locate_elem(element):
    if element in fibonacci_seq:
        print(f"The number - {element} is at index {fibonacci_seq.index(element)}")
    else:
        print(f"The number {element} is not in the sequence")

def start_program():
    while True:
        command = input().split()
        if command[0] == "Stop":
            break
        if command[0] == "Create":
            create_fibonacci_seq(int(command[2]))
        elif command[0] == "Locate":
            locate_elem(int(command[1]))