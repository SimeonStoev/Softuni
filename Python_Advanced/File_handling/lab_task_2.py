import os
from Constants import *

file_path = os.path.join(path_to_dir, "Files", "numbers.txt")
sum_numbers = 0

try:
    with open(file_path) as file:
        for row in file:
            sum_numbers += int(row)
    print(sum_numbers)
except FileNotFoundError:
    print("File not found")
