word = input()
reverse_word = ""

for letter in reversed(word):
    reverse_word += letter

print(reverse_word)