#!/usr/bin/env python3
# pylint: disable=W0603
# pylint: disable=W0612
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=W0631
import os
import sys
import json
import warnings


UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'
SPECIAL = '-~!@#$%^&*_+=`|(){}[:;"\'<>,.? ]'
BLOCKLIST = json.load(open('blocklistWordsData.json', 'r'))
MINCLASSES = 1
LENGTH = 1

MUST_HAVE_LOWER = False
MUST_HAVE_UPPER = False
MUST_HAVE_DIGIT = False
MUST_HAVE_SPECIAL = False

LOWER_MAX = 0
LOWER_MIN = 0
UPPER_MAX = 0
UPPER_MIN = 0
DIGIT_MAX = 0
DIGIT_MIN = 0
SPECIAL_MAX = 0
SPECIAL_MIN = 0

LOWER_OCCURENCES_COMPLIANT = False
UPPER_OCCURENCES_COMPLIANT = False
DIGIT_OCCURENCES_COMPLIANT = False
SPECIAL_OCCURENCES_COMPLIANT = False
BLOCKLIST_COMPLIANT = True
MINCLASSES_COMPLIANT = True
LENGTH_COMPLIANT = False

CAN_HAVE_LOWER = False
CAN_HAVE_UPPER = False
CAN_HAVE_DIGIT = False
CAN_HAVE_SPECIAL = False

CHECK_BLOCKLIST = False
FAILED = 0


def has_upper(pw: str):
    global UPPER
    return any(ext in pw for ext in UPPER)


def has_lower(pw: str):
    global LOWER
    return any(ext in pw for ext in LOWER)


def has_digit(pw: str):
    global DIGIT
    return any(ext in pw for ext in DIGIT)


def has_special(pw: str):
    global SPECIAL
    return any(ext in pw for ext in SPECIAL)


def check_lower_occurrences_compliance(pw: str):
    global LOWER_MIN
    global LOWER_MAX
    global LOWER_OCCURENCES_COMPLIANT
    count = 0
    for c in pw:
        if c in LOWER:
            count += 1

    if count >= LOWER_MIN and count <= LOWER_MAX:
        LOWER_OCCURENCES_COMPLIANT = True


def check_upper_occurrences_compliance(pw: str):
    global UPPER_MIN
    global UPPER_MAX
    global UPPER_OCCURENCES_COMPLIANT
    count = 0
    for c in pw:
        if c in UPPER:
            count += 1
    if count >= UPPER_MIN and count <= UPPER_MAX:
        UPPER_OCCURENCES_COMPLIANT = True


def check_digit_occurrences_compliance(pw: str):
    global DIGIT_MIN
    global DIGIT_MAX
    global DIGIT_OCCURENCES_COMPLIANT
    count = 0
    for c in pw:
        if c in DIGIT:
            count += 1

    if count >= DIGIT_MIN and count <= DIGIT_MAX:
        DIGIT_OCCURENCES_COMPLIANT = True


def check_special_occurrences_compliance(pw: str):
    global SPECIAL_MIN
    global SPECIAL_MAX
    global SPECIAL_OCCURENCES_COMPLIANT
    count = 0
    for c in pw:
        if c in SPECIAL:
            count += 1

    if count >= SPECIAL_MIN and count <= SPECIAL_MAX:
        SPECIAL_OCCURENCES_COMPLIANT = True


def check_blocklist_compliance(pw: str):
    global BLOCKLIST_COMPLIANT
    for b in BLOCKLIST["blocklist"]:
        if b in pw:
            # print("blocklist word => ", b)
            BLOCKLIST_COMPLIANT = False


def check_minclasses_compliance(pw: str):
    global MINCLASSES_COMPLIANT
    lower = 0
    upper = 0
    digit = 0
    special = 0
    for l in pw:
        if l in LOWER:
            lower = 1
        elif l in UPPER:
            upper = 1
        elif l in DIGIT:
            digit = 1
        elif l in SPECIAL:
            special = 1

    if (lower+upper+digit+special) < MINCLASSES:
        MINCLASSES_COMPLIANT = False


def check_length_compliance(pw: str):
    global LENGTH_COMPLIANT
    if len(pw) == LENGTH:
        LENGTH_COMPLIANT = True
    else:
        LENGTH_COMPLIANT = False


def read_policy():
    global MINCLASSES
    global MUST_HAVE_LOWER
    global MUST_HAVE_UPPER
    global MUST_HAVE_DIGIT
    global MUST_HAVE_SPECIAL
    global CAN_HAVE_LOWER
    global CAN_HAVE_UPPER
    global CAN_HAVE_DIGIT
    global CAN_HAVE_SPECIAL
    global LOWER_MAX
    global LOWER_MIN
    global UPPER_MAX
    global UPPER_MIN
    global DIGIT_MAX
    global DIGIT_MIN
    global SPECIAL_MAX
    global SPECIAL_MIN
    global CHECK_BLOCKLIST
    global LENGTH

    if int(sys.argv[2]) > 0:
        LENGTH = int(sys.argv[2])
    if int(sys.argv[3]) > 0:
        MUST_HAVE_LOWER = True
        CAN_HAVE_LOWER = True
        LOWER_MAX = int(sys.argv[4])
        LOWER_MIN = int(sys.argv[3])
    if int(sys.argv[3]) == 0 and int(sys.argv[4]) > 0:
        MUST_HAVE_LOWER = False
        CAN_HAVE_LOWER = True
        LOWER_MAX = int(sys.argv[4])
        LOWER_MIN = int(sys.argv[3])
    if int(sys.argv[3]) == 0 and int(sys.argv[4]) == 0:
        MUST_HAVE_LOWER = False
        CAN_HAVE_LOWER = False
        LOWER_MAX = int(sys.argv[4])
        LOWER_MIN = int(sys.argv[3])
    # upper policy
    if int(sys.argv[5]) > 0:
        MUST_HAVE_UPPER = True
        CAN_HAVE_UPPER = True
        UPPER_MAX = int(sys.argv[6])
        UPPER_MIN = int(sys.argv[5])
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) > 0:
        MUST_HAVE_UPPER = False
        CAN_HAVE_UPPER = True
        UPPER_MAX = int(sys.argv[6])
        UPPER_MIN = int(sys.argv[5])
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) == 0:
        MUST_HAVE_UPPER = False
        CAN_HAVE_UPPER = False
        UPPER_MAX = int(sys.argv[6])
        UPPER_MIN = int(sys.argv[5])
    # digit policy
    if int(sys.argv[7]) > 0:
        MUST_HAVE_DIGIT = True
        CAN_HAVE_DIGIT = True
        DIGIT_MAX = int(sys.argv[8])
        DIGIT_MIN = int(sys.argv[7])
    if int(sys.argv[7]) == 0 and int(sys.argv[8]) > 0:
        MUST_HAVE_DIGIT = False
        CAN_HAVE_DIGIT = True
        DIGIT_MAX = int(sys.argv[8])
        DIGIT_MIN = int(sys.argv[7])
    if int(sys.argv[7]) == 0 and int(sys.argv[8]) == 0:
        MUST_HAVE_DIGIT = False
        CAN_HAVE_DIGIT = False
        DIGIT_MAX = int(sys.argv[8])
        DIGIT_MIN = int(sys.argv[7])
    # special policy
    if int(sys.argv[9]) > 0:
        MUST_HAVE_SPECIAL = True
        CAN_HAVE_SPECIAL = True
        SPECIAL_MAX = int(sys.argv[10])
        SPECIAL_MIN = int(sys.argv[9])
    if int(sys.argv[9]) == 0 and int(sys.argv[10]) > 0:
        MUST_HAVE_SPECIAL = False
        CAN_HAVE_SPECIAL = True
        SPECIAL_MAX = int(sys.argv[10])
        SPECIAL_MIN = int(sys.argv[9])
    if int(sys.argv[9]) == 0 and int(sys.argv[10]) == 0:
        MUST_HAVE_SPECIAL = False
        CAN_HAVE_SPECIAL = False
        SPECIAL_MAX = int(sys.argv[10])
        SPECIAL_MIN = int(sys.argv[9])
    # minclasses
    if '--minclasses' in sys.argv:
        index = sys.argv.index('--minclasses')
        arg_length = len(sys.argv)
        # no more values after --minclasses
        if (arg_length == index + 1):
            warnings.warn(
                "--minclasses argument will not be read. It's missing a value.")
        # more values after --minclasses
        elif (arg_length > index + 1):
            # no value after, only another argument option
            if (sys.argv[index + 1] == '--blocklist'):
                warnings.warn(
                    "--minclasses argument will not be read. It's missing a value.")
            # next is a number
            elif (int(sys.argv[index + 1]) >= 1 and int(sys.argv[index + 1]) <= 4):
                MINCLASSES = int(sys.argv[index + 1])
            else:
                raise ValueError(
                    '--minclasses <value> : <value> should be an int between 1 and 4.')

    # blocklist
    if '--blocklist' in sys.argv:
        CHECK_BLOCKLIST = True


def check_failure(pw: str):
    global MUST_HAVE_LOWER
    global MUST_HAVE_UPPER
    global MUST_HAVE_DIGIT
    global MUST_HAVE_SPECIAL
    global CAN_HAVE_LOWER
    global CAN_HAVE_UPPER
    global CAN_HAVE_DIGIT
    global CAN_HAVE_SPECIAL
    global LOWER_OCCURENCES_COMPLIANT
    global UPPER_OCCURENCES_COMPLIANT
    global DIGIT_OCCURENCES_COMPLIANT
    global SPECIAL_OCCURENCES_COMPLIANT
    global FAILED

    # check occurrences compliance
    check_lower_occurrences_compliance(pw)
    check_upper_occurrences_compliance(pw)
    check_digit_occurrences_compliance(pw)
    check_special_occurrences_compliance(pw)
    check_blocklist_compliance(pw)
    check_minclasses_compliance(pw)
    check_length_compliance(pw)

    # has lower and cannot have it
    if has_lower(pw) and not MUST_HAVE_LOWER and not CAN_HAVE_LOWER:
        print("CANNOT HAVE LOWER")
        FAILED += 1
        print("failed => ", pw)
        return
    # doesn't have lower and it must have it
    elif not has_lower(pw) and MUST_HAVE_LOWER:
        print("MUST HAVE LOWER")
        FAILED += 1
        print("failed => ", pw)
        return
    # has lower but it is not compliant with specifications of occurrences
    elif has_lower(pw) and not LOWER_OCCURENCES_COMPLIANT:
        print("LOWER OCCURENCES")
        FAILED += 1
        print("failed => ", pw)
        return

    elif has_upper(pw) and not MUST_HAVE_UPPER and not CAN_HAVE_UPPER:
        print("CANNOT HAVE UPPER")
        FAILED += 1
        print("failed => ", pw)
        return
    elif not has_upper(pw) and MUST_HAVE_UPPER:
        print("MUST HAVE UPPER")
        FAILED += 1
        print("failed => ", pw)
        return
    # has upper but it is not compliant with specifications of occurrences
    elif has_upper(pw) and not UPPER_OCCURENCES_COMPLIANT:
        print("UPPER OCCURENCES")
        FAILED += 1
        print("failed => ", pw)
        return
    elif has_digit(pw) and not MUST_HAVE_DIGIT and not CAN_HAVE_DIGIT:
        print("CANNOT HAVE DIGIT")
        FAILED += 1
        print("failed => ", pw)
        return
    elif not has_digit(pw) and MUST_HAVE_DIGIT:
        print("MUST HAVE DIGIT")
        FAILED += 1
        print("failed => ", pw)
        return
    # has digit but it is not compliant with specifications of occurrences
    elif has_digit(pw) and not DIGIT_OCCURENCES_COMPLIANT:
        print("DIGIT OCCURENCES")
        FAILED += 1
        print("failed => ", pw)
        return
    elif has_special(pw) and not MUST_HAVE_SPECIAL and not CAN_HAVE_SPECIAL:
        print("CANNOT HAVE SPECIAL")
        FAILED += 1
        print("failed => ", pw)
        return
    elif not has_special(pw) and MUST_HAVE_SPECIAL:
        print("MUST HAVE SPECIAL")
        FAILED += 1
        print("failed => ", pw)
        return
    # has special but it is not compliant with specifications of occurrences
    elif has_special(pw) and not SPECIAL_OCCURENCES_COMPLIANT:
        print("SPECIAL OCCURENCES")
        FAILED += 1
        print("failed => ", pw)
        return
    # failed the blocklist test. This means that there is a breached password as a substring of the generated password
    elif CHECK_BLOCKLIST and not BLOCKLIST_COMPLIANT:
        print("BLOCKLIST")
        FAILED += 1
        print("failed => ", pw)
        return
    elif not MINCLASSES_COMPLIANT:
        print("MINCLASSES")
        FAILED += 1
        print("failed => ", pw)
        return
    elif not LENGTH_COMPLIANT:
        print("LENGTH")
        FAILED += 1
        print("failed => ", pw)
        return


def main():
    global LOWER_OCCURENCES_COMPLIANT
    global UPPER_OCCURENCES_COMPLIANT
    global DIGIT_OCCURENCES_COMPLIANT
    global SPECIAL_OCCURENCES_COMPLIANT
    global BLOCKLIST_COMPLIANT
    global MINCLASSES_COMPLIANT
    global FAILED
    global LENGTH_COMPLIANT

    total_pws_checked = 0
    total_pws_failed = 0

    allowed_args = ['--blocklist', '--minclasses']
    if len(sys.argv) > 15:
        raise ValueError(
            'Please provide the folder that contains the files of pws that you want to check and the policy to check against.')
    elif len(sys.argv) < 11:
        raise ValueError(
            'Error. Missing arguments. Check the README to understand how to use the script.')
    elif (len(sys.argv) == 12 and sys.argv[11] not in allowed_args) or (len(sys.argv) == 14 and (allowed_args[0] not in sys.argv or allowed_args[1] not in sys.argv)):
        raise ValueError(
            'Error. Unknown argument. Did you mispelled?')

    # elif len(sys.argv) == 13 and sys.argv[11] not in allowed_args:
        # start = time.time()
    list_of_files = []
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            list_of_files.append(os.path.join(root, file))

    # read and interpret the policy
    read_policy()
    ##
    # leaving this here to read just one simple file, for testing of the program
    # with open(f"{sys.argv[1]}", 'r') as fp:
    #     for count, line in enumerate(fp):
    #         check_lower_occurrences_compliance(line)
    #         check_upper_occurrences_compliance(line)
    #         check_digit_occurrences_compliance(line)
    #         check_special_occurrences_compliance(line)
    #         check_failure(line)
    #         LOWER_OCCURENCES_COMPLIANT = False
    #         UPPER_OCCURENCES_COMPLIANT = False
    #         DIGIT_OCCURENCES_COMPLIANT = False
    #         SPECIAL_OCCURENCES_COMPLIANT = False

    #     total_lines = count + 1
    #     failed_percentage = failed / total_lines
    #     print(f'File Analyzed: {sys.argv[1]}')
    #     print('Total Passwords Analyzed:', total_lines)
    #     print('Total Compliant Passwords:', total_lines - failed)
    #     print('Total Non-Compliant Passwords:', failed)
    #     print(f'Failed Percentage: {failed_percentage*100}%\n')

    for file in list_of_files:
        FAILED = 0
        with open(f"{file}", 'r') as fp:
            for count, line in enumerate(fp):
                # check for overall pw compliance
                check_failure(line.strip())
                # reset values for next iteration
                LOWER_OCCURENCES_COMPLIANT = False
                UPPER_OCCURENCES_COMPLIANT = False
                DIGIT_OCCURENCES_COMPLIANT = False
                SPECIAL_OCCURENCES_COMPLIANT = False
                BLOCKLIST_COMPLIANT = True
                MINCLASSES_COMPLIANT = True
                LENGTH_COMPLIANT = False

            total_file_lines = count + 1
            total_pws_checked += total_file_lines
            total_pws_failed += FAILED
            file_failed_percentage = FAILED / total_file_lines
            print(f'File Analyzed: {file}')
            print('Total Passwords Analyzed:', total_file_lines)
            print('Total Compliant Passwords:', total_file_lines - FAILED)
            print('Total Non-Compliant Passwords:', FAILED)
            print(f'Failed Percentage: {file_failed_percentage*100}%\n')

    overall_failed_percentage = (total_pws_failed / total_pws_checked) * 100
    print(f'Total Files Analyzed: {len(list_of_files)}')
    print('Total Passwords Analyzed:', total_pws_checked)
    print('Total Compliant Passwords:', total_pws_checked - total_pws_failed)
    print('Total Non-Compliant Passwords:', total_pws_failed)
    print(f'Failed Percentage: {overall_failed_percentage}%\n')
    # end = time.time()
    # print("\n\n" + str(round(end-start, 2)) + " secs which is ")
    # print(str(round(end-start, 2)/60) + " mins")


if __name__ == "__main__":
    main()
