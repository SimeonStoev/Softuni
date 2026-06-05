import os
import string

import Constants

file_path = os.path.join(Constants.path_to_dir, "Files", "text.txt")
new_file_path = os.path.join(Constants.path_to_dir, "Files", "another_text.txt")

try:
    with open(file_path, "r") as file:
        line_number = 0
        for line in file.readlines():
            line_number += 1
            line_str = f"Line {line_number}: "
            new_line = line_str + line
            count_letters = sum(1 for ch in line if ch.isalpha())
            count_punc = sum(1 for ch in line if ch in string.punctuation)
            try:
                with open(new_file_path, "a") as file:
                    file.write(new_line.rstrip("\n") + f" ({count_letters})({count_punc})" + "\n")
            except FileNotFoundError:
                print("File not found")
except FileNotFoundError:
    print("File not found")
