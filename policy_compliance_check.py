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

lower_max = 0
lower_min = 0
upper_max = 0
upper_min = 0
digit_max = 0
digit_min = 0
special_max = 0
special_min = 0

lower_occurences_compliant = False
upper_occurences_compliant = False
digit_occurences_compliant = False
special_occurences_compliant = False

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


def check_lower_occurrences_compliance(pw: str):
    global lower_min
    global lower_max
    global lower_occurences_compliant
    count = 0
    for c in pw:
        if c in LOWER:
            count += 1

    if count >= lower_min and count <= lower_max:
        lower_occurences_compliant = True


def check_upper_occurrences_compliance(pw: str):
    global upper_min
    global upper_max
    global upper_occurences_compliant
    count = 0
    for c in pw:
        if c in UPPER:
            count += 1
    if count >= upper_min and count <= upper_max:
        upper_occurences_compliant = True


def check_digit_occurrences_compliance(pw: str):
    global digit_min
    global digit_max
    global digit_occurences_compliant
    count = 0
    for c in pw:
        if c in DIGIT:
            count += 1

    if count >= digit_min and count <= digit_max:
        digit_occurences_compliant = True


def check_special_occurrences_compliance(pw: str):
    global special_min
    global special_max
    global special_occurences_compliant
    count = 0
    for c in pw:
        if c in DIGIT:
            count += 1

    if count >= special_min and count <= special_max:
        special_occurences_compliant = True


def read_policy():
    global must_have_lower
    global must_have_upper
    global must_have_digit
    global must_have_special
    global can_have_lower
    global can_have_upper
    global can_have_digit
    global can_have_special
    global lower_max
    global lower_min
    global upper_max
    global upper_min
    global digit_max
    global digit_min
    global special_max
    global special_min

    if int(sys.argv[3]) > 0:
        must_have_lower = True
        can_have_lower = True
        lower_max = int(sys.argv[4])
        lower_min = int(sys.argv[3])
    if int(sys.argv[3]) == 0 and int(sys.argv[4]) > 0:
        must_have_lower = False
        can_have_lower = True
        lower_max = int(sys.argv[4])
        lower_min = int(sys.argv[3])
    if int(sys.argv[3]) == 0 and int(sys.argv[4]) == 0:
        must_have_lower = False
        can_have_lower = False
        lower_max = int(sys.argv[4])
        lower_min = int(sys.argv[3])
    # upper policy
    if int(sys.argv[5]) > 0:
        must_have_upper = True
        can_have_upper = True
        upper_max = int(sys.argv[6])
        upper_min = int(sys.argv[5])
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) > 0:
        must_have_upper = False
        can_have_upper = True
        upper_max = int(sys.argv[6])
        upper_min = int(sys.argv[5])
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) == 0:
        must_have_upper = False
        can_have_upper = False
        upper_max = int(sys.argv[6])
        upper_min = int(sys.argv[5])
    # digit policy
    if int(sys.argv[7]) > 0:
        must_have_digit = True
        can_have_digit = True
        digit_max = int(sys.argv[8])
        digit_min = int(sys.argv[7])
    if int(sys.argv[7]) == 0 and int(sys.argv[8]) > 0:
        must_have_digit = False
        can_have_digit = True
        digit_max = int(sys.argv[8])
        digit_min = int(sys.argv[7])
    if int(sys.argv[7]) == 0 and int(sys.argv[8]) == 0:
        must_have_digit = False
        can_have_digit = False
        digit_max = int(sys.argv[8])
        digit_min = int(sys.argv[7])
    # special policy
    if int(sys.argv[9]) > 0:
        must_have_special = True
        can_have_special = True
        special_max = int(sys.argv[10])
        special_min = int(sys.argv[9])
    if int(sys.argv[9]) == 0 and int(sys.argv[10]) > 0:
        must_have_special = False
        can_have_special = True
        special_max = int(sys.argv[10])
        special_min = int(sys.argv[9])
    if int(sys.argv[9]) == 0 and int(sys.argv[10]) == 0:
        must_have_special = False
        can_have_special = False
        special_max = int(sys.argv[10])
        special_min = int(sys.argv[9])


def check_failure(pw: str):
    global must_have_lower
    global must_have_upper
    global must_have_digit
    global must_have_special
    global can_have_lower
    global can_have_upper
    global can_have_digit
    global can_have_special
    global lower_occurences_compliant
    global upper_occurences_compliant
    global digit_occurences_compliant
    global special_occurences_compliant
    global failed
    check_lower_occurrences_compliance(pw)
    check_upper_occurrences_compliance(pw)
    check_digit_occurrences_compliance(pw)
    check_special_occurrences_compliance(pw)
    # print(f"READING THIS PW => {pw}")
    # has lower and cannot have it
    if has_lower(pw) and not must_have_lower and not can_have_lower:
        # print("CANNOT HAVE LOWER")
        failed += 1
        return
    # doesn't have lower and it must have it
    elif not has_lower(pw) and must_have_lower:
        # print("MUST HAVE LOWER")
        failed += 1
        return
    # has lower but it is not compliant with specifications of occurrences
    elif has_lower(pw) and not lower_occurences_compliant:
        # print("LOWER OCCURENCES")
        failed += 1
        return

    elif has_upper(pw) and not must_have_upper and not can_have_upper:
        # print("CANNOT HAVE UPPER")
        failed += 1
        return
    elif not has_upper(pw) and must_have_upper:
        # print("MUST HAVE UPPER")
        failed += 1
        return
    # has upper but it is not compliant with specifications of occurrences
    elif has_upper(pw) and not upper_occurences_compliant:
        # print("UPPER OCCURENCES")
        failed += 1
        return
    elif has_digit(pw) and not must_have_digit and not can_have_digit:
        # print("CANNOT HAVE DIGIT")
        failed += 1
        return
    elif not has_digit(pw) and must_have_digit:
        #print("MUST HAVE DIGIT")
        failed += 1
        return
    # has digit but it is not compliant with specifications of occurrences
    elif has_digit(pw) and not digit_occurences_compliant:
        #print("DIGIT OCCURENCES")
        failed += 1
        return
    elif has_special(pw) and not must_have_special and not can_have_special:
        #print("CANNOT HAVE SPECIAL")
        failed += 1
        return
    elif not has_special(pw) and must_have_special:
        #print("MUST HAVE SPECIAL")

        failed += 1
        return
    # has special but it is not compliant with specifications of occurrences
    elif has_special(pw) and not special_occurences_compliant:
        #print("SPECIAL OCCURENCES")

        failed += 1
        return


def main():
    global lower_occurences_compliant
    global upper_occurences_compliant
    global digit_occurences_compliant
    global special_occurences_compliant
    global failed

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
    #         lower_occurences_compliant = False
    #         upper_occurences_compliant = False
    #         digit_occurences_compliant = False
    #         special_occurences_compliant = False

    #     total_lines = count + 1
    #     failed_percentage = failed / total_lines
    #     print(f'File Analyzed: {sys.argv[1]}')
    #     print('Total Passwords Analyzed:', total_lines)
    #     print('Total Compliant Passwords:', total_lines - failed)
    #     print('Total Non-Compliant Passwords:', failed)
    #     print(f'Failed Percentage: {failed_percentage*100}%\n')

    for file in list_of_files:
        failed = 0
        with open(f"{file}", 'r') as fp:
            for count, line in enumerate(fp):
                # check occurrences compliance
                check_lower_occurrences_compliance(line)
                check_upper_occurrences_compliance(line)
                check_digit_occurrences_compliance(line)
                check_special_occurrences_compliance(line)
                # check for overall pw compliance
                check_failure(line)
                # reset values for next iteration
                lower_occurences_compliant = False
                upper_occurences_compliant = False
                digit_occurences_compliant = False
                special_occurences_compliant = False

            total_file_lines = count + 1
            total_pws_checked += total_file_lines
            total_pws_failed += failed
            file_failed_percentage = failed / total_file_lines
            print(f'File Analyzed: {file}')
            print('Total Passwords Analyzed:', total_file_lines)
            print('Total Compliant Passwords:', total_file_lines - failed)
            print('Total Non-Compliant Passwords:', failed)
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
