import os
import Constants
import re

try:
    words_file = open(os.path.join(Constants.path_to_dir, "Files", "words.txt"))
    list_of_words = words_file.read().split()
    words_dict = {word: 0 for word in list_of_words}

    try:
        text_file = open(os.path.join(Constants.path_to_dir, "Files", "text.txt"))
        for text_file_row in text_file:
            for word in list_of_words:
                count_word = len(re.findall(r"\b" + word + r"\b", text_file_row, re.IGNORECASE))
                if count_word > 0:
                    words_dict[word] += count_word

        sorted_word_dict = dict(sorted(words_dict.items(), key= lambda x: -x[1]))
        for key, value in sorted_word_dict.items():
            print(f"{key} - {value}")
    except FileNotFoundError:
        print("File text.txt not found.")
    finally:
        text_file.close()

except FileNotFoundError:
    print("File words.txt not found")
finally:
    words_file.close()