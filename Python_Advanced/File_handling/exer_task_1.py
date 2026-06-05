import os
import Constants
import re

file_path = os.path.join(Constants.path_to_dir, "Files", "text1.txt")

try:
    with open(file_path, "r") as file:
        row = -1
        for line in file.readlines():
            row += 1
            if row % 2 == 0:
                replaced_line = re.sub(r"[-,.!?]", "@", line)
                replaced_line_list = replaced_line.split()
                replaced_line_list.reverse()
                print(" ".join(replaced_line_list))
except FileNotFoundError:
    print("File not found")
