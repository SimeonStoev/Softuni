import os
from pathlib import Path

import Constants

files = {}


def get_files(folder, level):
    if level == 2:
        return

    for file in os.listdir(folder):
        current_path = os.path.join(folder, file)

        if os.path.isfile(current_path):
            ext = Path(file).suffix
            if "." in ext:
                files.setdefault(ext[1:], []).append(file)
        elif os.path.isdir(current_path):
            get_files(current_path, level + 1)

    return


get_files(Constants.path_to_dir, 0)

files_ordered = dict(sorted(files.items(), key=lambda x: (x[0].lower(), x[1])))

for key, value in files_ordered.items():
    print(f".{key}")
    for file in value:
        print(f"- - - {file}")
