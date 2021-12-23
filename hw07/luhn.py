# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw07
# Name: Kejian Tong

def double_sum_digits(digit):
    """
    This is doubling the digits and adding them together
    """
    DOUBLE_DIGIT = 2  # Constant value

    double_sum = digit * DOUBLE_DIGIT  # Doubles the number
    # Converting the num into string the into a list
    digits_list = list(str(double_sum))

    # if the length of that result is still greater than 1
    # which means it is like 18 or 14, then sum the digits
    if len(digits_list) > 1:
        # this is adding them all together
        double_sum = sum([int(d) for d in digits_list])
    return double_sum


def luhns(input_string):
    """
    Compute the results using for loop and return the sum values
    """
    # Constant values
    NEG_DOUB_DIGIT = -2
    POS_DOUB_DIGIT = 2
    DIVISOR_DIGIT = 10

    int_list = [int(n) for n in input_string]  # Converts str to list of int

    for i in range(len(int_list) - POS_DOUB_DIGIT, -1, NEG_DOUB_DIGIT):
        int_list[i] = double_sum_digits(int_list[i])
    return sum(int_list) % DIVISOR_DIGIT == 0


def main():
    """
    Call other function
    """
    input_string = input("Please input numbers: ")
    if luhns(input_string):
        print("Valid number")
    else:
        print("Not Valid number")


main()
