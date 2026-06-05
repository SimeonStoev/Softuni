from email.generator import fcre

import Constants
import os

try:
    f = open(os.path.join(Constants.path_to_dir, "Files", "text.txt"))
    print("File found")
except FileNotFoundError:
    print("File not found")
finally:
    f.close()
