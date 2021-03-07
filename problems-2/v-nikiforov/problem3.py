import os
import sys
from os.path import isfile, join

if len(sys.argv) == 2:
    path = sys.argv[1]
    files_sizes = (
        (join(path, i), os.stat(join(path, i)).st_size)
        for i in os.listdir(path)
        if isfile(join(path, i))
    )
    for i, j in sorted(files_sizes, key=lambda x: (x[1], x[0])):
        print(f"{i} - {j} bytes")
else:
    raise Exception("You have to specify file path as a fist argument")
