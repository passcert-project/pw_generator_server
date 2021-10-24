#!/usr/bin/env python3
# pylint: disable=W0603
# pylint: disable=W0612
# pylint: disable=C0111
# pylint: disable=C0103
import os
import sys
import json


UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'
SPECIAL = '-~!@#$%^&*_+=`|(){}[:;"\'<>,.? ]'
BLOCKLIST = json.load(open('blocklistWordsData.json', 'r'))

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

CAN_HAVE_LOWER = False
CAN_HAVE_UPPER = False
CAN_HAVE_DIGIT = False
CAN_HAVE_SPECIAL = False

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


def check_blocklist_compliant(pw: str):
    global BLOCKLIST_COMPLIANT
    for b in BLOCKLIST["blocklist"]:
        if b in pw:
            BLOCKLIST_COMPLIANT = False


def read_policy():
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
    check_lower_occurrences_compliance(pw)
    check_upper_occurrences_compliance(pw)
    check_digit_occurrences_compliance(pw)
    check_special_occurrences_compliance(pw)
    # print(f"READING THIS PW => {pw}")
    # has lower and cannot have it
    if has_lower(pw) and not MUST_HAVE_LOWER and not CAN_HAVE_LOWER:
        # print("CANNOT HAVE LOWER")
        FAILED += 1
        return
    # doesn't have lower and it must have it
    elif not has_lower(pw) and MUST_HAVE_LOWER:
        # print("MUST HAVE LOWER")
        FAILED += 1
        return
    # has lower but it is not compliant with specifications of occurrences
    elif has_lower(pw) and not LOWER_OCCURENCES_COMPLIANT:
        # print("LOWER OCCURENCES")
        FAILED += 1
        return

    elif has_upper(pw) and not MUST_HAVE_UPPER and not CAN_HAVE_UPPER:
        # print("CANNOT HAVE UPPER")
        FAILED += 1
        return
    elif not has_upper(pw) and MUST_HAVE_UPPER:
        # print("MUST HAVE UPPER")
        FAILED += 1
        return
    # has upper but it is not compliant with specifications of occurrences
    elif has_upper(pw) and not UPPER_OCCURENCES_COMPLIANT:
        # print("UPPER OCCURENCES")
        FAILED += 1
        return
    elif has_digit(pw) and not MUST_HAVE_DIGIT and not CAN_HAVE_DIGIT:
        # print("CANNOT HAVE DIGIT")
        FAILED += 1
        return
    elif not has_digit(pw) and MUST_HAVE_DIGIT:
        #print("MUST HAVE DIGIT")
        FAILED += 1
        return
    # has digit but it is not compliant with specifications of occurrences
    elif has_digit(pw) and not DIGIT_OCCURENCES_COMPLIANT:
        #print("DIGIT OCCURENCES")
        FAILED += 1
        return
    elif has_special(pw) and not MUST_HAVE_SPECIAL and not CAN_HAVE_SPECIAL:
        #print("CANNOT HAVE SPECIAL")
        FAILED += 1
        return
    elif not has_special(pw) and MUST_HAVE_SPECIAL:
        #print("MUST HAVE SPECIAL")
        FAILED += 1
        return
    # has special but it is not compliant with specifications of occurrences
    elif has_special(pw) and not SPECIAL_OCCURENCES_COMPLIANT:
        #print("SPECIAL OCCURENCES")
        FAILED += 1
        return
    # failed the blocklist test. This means that there is a breached password as a substring of the generated password
    elif not BLOCKLIST_COMPLIANT:
        FAILED += 1
        return


def main():
    global LOWER_OCCURENCES_COMPLIANT
    global UPPER_OCCURENCES_COMPLIANT
    global DIGIT_OCCURENCES_COMPLIANT
    global SPECIAL_OCCURENCES_COMPLIANT
    global BLOCKLIST_COMPLIANT
    global FAILED

    total_pws_checked = 0
    total_pws_failed = 0

    if len(sys.argv) != 11:
        raise ValueError(
            'Please provide the file that has the pws that you want to check and the policy to check against.')
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
                # check occurrences compliance
                check_lower_occurrences_compliance(line)
                check_upper_occurrences_compliance(line)
                check_digit_occurrences_compliance(line)
                check_special_occurrences_compliance(line)
                check_blocklist_compliant(line)
                # check for overall pw compliance
                check_failure(line)
                # reset values for next iteration
                LOWER_OCCURENCES_COMPLIANT = False
                UPPER_OCCURENCES_COMPLIANT = False
                DIGIT_OCCURENCES_COMPLIANT = False
                SPECIAL_OCCURENCES_COMPLIANT = False
                BLOCKLIST_COMPLIANT = True

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
