import os
import sys
import re

def remove_files(directory):
    files = os.listdir(directory)

    for file in files:

        pattern = r"^\_\_[a-zA-Z]"
        result = re.match(pattern, file)

        if result != None:
            os.remove(file)


remove_files()
    