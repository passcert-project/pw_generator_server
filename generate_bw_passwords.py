#!/usr/bin/env python3
import subprocess
import time
import sys

if len(sys.argv) != 3:
    raise ValueError(
        'Please provide the number of pws you want and the file name to save it to.')
start = time.time()
for i in range(int(sys.argv[1])):
    result = subprocess.run(
        ["bw", "generate"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    textfile = open(f"{sys.argv[2]}", "a")
    a = textfile.write(f'{result}\n')
    textfile.close()
end = time.time()
print(str(round(end-start, 2)) + " secs which is ")
print(str(round(end-start, 2)/60) + " mins")
