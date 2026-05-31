try:
    text = input()
    times = int(input())

    for i in range(1,times):
        text += text

    print(text)
except ValueError:
    print("Variable times must be an integer")
