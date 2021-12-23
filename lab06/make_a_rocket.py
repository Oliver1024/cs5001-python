# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab06
# Name: Kejian Tong

import sys

# Assign values to variable and constant
HALF_NUM = 2
argument_num = 4


def nose_cone(width):
    """Draw the nose cone of rocket
       Number -> None
    """
    # Assign value to variable
    half = width // HALF_NUM

    # Using for loop to get the nose part of rocket
    for line in range(half):
        print_nose = ""
        print_nose += " " * (half - line)
        print_nose += "*" * (width - ((half - line) * HALF_NUM))
        print(print_nose)


def body_part(width, length, style=None):
    """Draw the body part of rocket
       Number Number None -> None
    """
    half = width // HALF_NUM
    for _ in range(length):
        if(style == "striped"):
            for i in range(half):
                print("_" * width)
            for i in range(width - half):
                print("X" * width)
        else:
            for i in range(width):
                print("X" * width)


def tail_part(width):
    """ Get the tail part of rocket
        Number -> None
    """
    # Assign values to variables
    half = width // HALF_NUM
    quarter = half // HALF_NUM

    # Using for loop to get the tail part of rocket
    for i in range(quarter, half + 1):
        print(" " * (half - i) + "*" * (width - HALF_NUM * (half - i)))
    print("*" * width)


def main():
    """ Call other functions
        None -> None
    """
    width = int(sys.argv[1])
    length = int(sys.argv[2])
    if len(sys.argv) >= argument_num:
        style = sys.argv[3]
        nose_cone(width)
        body_part(width, length, style)
        tail_part(width)
    else:
        nose_cone(width)
        body_part(width, length)
        tail_part(width)


main()
