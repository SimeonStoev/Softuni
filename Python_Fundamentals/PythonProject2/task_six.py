import math

word = ""
most_powerful_word = ""
most_powerful_word_power = 0

while word != "End of words":
    word = input()
    if word != "End of words":
        word_power = 0
        vowels = ("a", "e", "i", "o", "u", 'y')
        starts_with_vowel = False
        if word.lower().startswith(vowels):
            starts_with_vowel = True
        for letter in word:
            word_power += ord(letter)

        if starts_with_vowel:
            word_power *= len(word)
        else:
            word_power /= len(word)
            word_power = math.floor(word_power)

        if word_power > most_powerful_word_power:
            most_powerful_word = word
            most_powerful_word_power = word_power

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_power}")
