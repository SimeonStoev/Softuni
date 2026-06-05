import os
import Constants

file_path = os.path.join(Constants.path_to_dir, "Files", "my_first_file.txt")

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File already deleted!")
