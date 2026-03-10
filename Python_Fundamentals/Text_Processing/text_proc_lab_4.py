banned_words = input().split(", ")
string = input()

for banned_word in banned_words:
    banned_word_len = len(banned_word)
    while banned_word in string:
        string = string.replace(banned_word, "*" * banned_word_len)

print(string)
