import os
import path

source_directory = 'Text_file'
file1 = 'p1.txt'
file2 = 'p1.txt'
filelist = [file1, file2]

passagelist = []

for afile in filelist:
    path = os.path.join(source_directory, afile)
    with open(path, 'r', newline='') as f:
        passagelist.append(f.read())
