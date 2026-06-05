import os
import Constants

path_to_new_file = os.path.join(Constants.path_to_dir, "Files")

print(path_to_new_file)

try:
    f = open(os.path.join(path_to_new_file, "my_first_file.txt"), "w")
    f.write("I just created my first file!")
except FileNotFoundError:
    print("Error creating file")
finally:
    f.close()
