text_filter = [word for word in input().split() if len(word) % 2 == 0]

for word in text_filter:
    print(word)
