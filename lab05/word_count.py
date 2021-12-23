"""
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab05
Name: Kejian Tong
"""

import re

# Get input file from user
files = input("Please enter the file name: ")


def main():
    """
    Here is the maina function that is used to open the file.
    When the file does not exist, it will prompt the user
    that it cannot be opened.
    """
    try:
        f = open(files, 'r')
        pass
    except FileNotFoundError as e:
        print("Can't open", files)
        return

    # Assign values to variables
    words_count = 0
    char_count = 0
    letters_count = 0

    # For loop is used to replace line by line according to some rules
    for line in f:
        per_line = line.replace(" ", "").rstrip()
        print(per_line)
        words = line.split()
        print(words)
        words_count += len(words)
        char_count += len(per_line)
        per_letter = re.sub(r'[^a-zA-Z0-9_]', '', line)
        letters_count += len(per_letter)

    # Print the results
    print("Words:", words_count)
    print("Characters", char_count)
    print("Letters & numbers:", letters_count)


main()
