#!/usr/bin/env python3
import os
import subprocess
import time
import sys

# bitwarden's default => -uln --length 14
# --uppercase, -u (include uppercase)
# --lowercase, -l (include lowercase)
# --number, -n (include numbers)
# --special, -s (include special characters)
# --length <length> (length of the password, min. of 5)
# bitwarden's default for jasmin => 14 1 14 1 14 1 14 0 0

# required: upper, lower, digit, symbol; minlength: 10;
# 14 1 14 1 14 1 14 1 14

# required: upper, lower, digit, symbol; minlength: 15;
# 15 1 15 1 15 1 15 1 15

if len(sys.argv) != 12:
    raise ValueError(
        'Please provide the number of pws you want to generate, the policy (length=9) and the file name to save it to.')
start = time.time()
for i in range(int(sys.argv[1])):

    result = subprocess.run(["./passwordGeneratorApp.out", "-a", f"{sys.argv[2]}", f"{sys.argv[3]}",
                             f"{sys.argv[4]}", f"{sys.argv[5]}", f"{sys.argv[6]}", f"{sys.argv[7]}", f"{sys.argv[8]}",
                             f"{sys.argv[9]}", f"{sys.argv[10]}"], stdout=subprocess.PIPE).stdout.decode('utf-8')

    result = result.split()
    textfile = open(f"{sys.argv[11]}", "a")
    a = textfile.write(f'{result[2]}\n')
    textfile.close()

end = time.time()
print(str(round(end-start, 2)) + " secs which is ")
print(str(round(end-start, 2)/60) + " mins")
