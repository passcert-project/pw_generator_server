#!/usr/bin/env python3
import os
import time
import sys

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'
SPECIAL = '-~!@#$%^&*_+=`|(){}[:;"\'<>,.? ]'

must_have_lower = False
must_have_upper = False
must_have_digit = False
must_have_special = False

can_have_lower = False
can_have_upper = False
can_have_digit = False
can_have_special = False

failed = 0


def has_upper(pw: str):
    return any(ext in pw for ext in UPPER)


def has_lower(pw: str):
    return any(ext in pw for ext in LOWER)


def has_digit(pw: str):
    return any(ext in pw for ext in DIGIT)


def has_special(pw: str):
    return any(ext in pw for ext in SPECIAL)


def read_policy():
    global must_have_lower
    global must_have_upper
    global must_have_digit
    global must_have_special
    global can_have_lower
    global can_have_upper
    global can_have_digit
    global can_have_special
    if int(sys.argv[3]) == 1:
        must_have_lower = True
        can_have_lower = True
    if int(sys.argv[3]) == 0 and int(sys.argv[4]) > 0:
        must_have_lower = False
        can_have_lower = True
    if int(sys.argv[3]) == 0 and int(sys.argv[4]) == 0:
        must_have_lower = False
        can_have_lower = False
    # upper policy
    if int(sys.argv[5]) == 1:
        must_have_upper = True
        can_have_upper = True
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) > 0:
        must_have_upper = False
        can_have_upper = True
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) == 0:
        must_have_upper = False
        can_have_upper = False
    # digit policy
    if int(sys.argv[7]) == 1:
        must_have_digit = True
        can_have_digit = True
    if int(sys.argv[7]) == 0 and int(sys.argv[8]) > 0:
        must_have_digit = False
        can_have_digit = True
    if int(sys.argv[7]) == 0 and int(sys.argv[8]) == 0:
        must_have_digit = False
        can_have_digit = False
    # special policy
    if int(sys.argv[9]) == 1:
        must_have_special = True
        can_have_special = True
    if int(sys.argv[9]) == 0 and int(sys.argv[10]) > 0:
        must_have_special = False
        can_have_special = True
    if int(sys.argv[9]) == 0 and int(sys.argv[10]) == 0:
        must_have_special = False
        can_have_special = False


def check_failure(pw: str):
    global must_have_lower
    global must_have_upper
    global must_have_digit
    global must_have_special
    global can_have_lower
    global can_have_upper
    global can_have_digit
    global can_have_special
    global failed

    if has_lower(pw) and not must_have_lower and not can_have_lower:
        failed = failed + 1
        return
    elif not has_lower(pw) and must_have_lower:
        failed = failed + 1
        return
    elif has_upper(pw) and not must_have_upper and not can_have_upper:
        failed = failed + 1
        return
    elif not has_upper(pw) and must_have_upper:
        failed = failed + 1
        return
    elif has_digit(pw) and not must_have_digit and not can_have_digit:
        failed = failed + 1
        return
    elif not has_digit(pw) and must_have_digit:
        failed = failed + 1
        return
    elif has_special(pw) and not must_have_special and not can_have_special:
        failed = failed + 1
        return
    elif not has_special(pw) and must_have_special:
        failed = failed + 1
        return


def main():
    if len(sys.argv) != 11:
        raise ValueError(
            'Please provide the file that has the pws that you want to check and the policy to check against.')
    start = time.time()

    # read and interpret the policy
    read_policy()

    with open(f"{sys.argv[1]}", 'r') as fp:
        for count, line in enumerate(fp):
            check_failure(line)

    # each line is a password. this will be used to calculate %
    total_lines = count + 1
    failed_percentage = failed / total_lines

    print('Total Passwords Analyzed:', count + 1)
    print('Total Non-Compliant Passwords:', failed)
    print(f'Failed %: {failed_percentage*100}%')
    end = time.time()
    print("\n\n" + str(round(end-start, 2)) + " secs which is ")
    print(str(round(end-start, 2)/60) + " mins")


if __name__ == "__main__":
    main()
