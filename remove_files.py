import os
import re

directory = os.getcwd()

def remove_files(directory):
    files = os.listdir(directory)

    for file in files:

        pattern = r"[a-zA-Z]\.txt"
        result = re.match(pattern, file)

        if result != None:
            os.remove(file)
    
    return os.listdir(directory)


remove_files(directory)
    