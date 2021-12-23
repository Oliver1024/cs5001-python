def my_input():
    """
    Prompt user to input number1 and number2 and return 2 numbers
    None ->  String String
    """
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")
    return number1, number2


def sum_fun(number1, number2):
    """
    Calculate the sum of number1 and number2
    String String -> None
    """
    list_rst = [int(number1), int(number2)]
    result = sum(list_rst)
    print(number1, "+", number2, "=", result)


def count_carry(number1, number2):
    """
    Count how many carries will there be when adding two numbers
    String String -> Number
    """
    # Assign values to variables
    carry = 0
    carries = 0
    len1 = len(number1)
    len2 = len(number2)

    # Using if and while loop to get carries when adding two numbers
    if (len1 < len2):
        while (len1 < len2):
            number1 = '0' + number1
            len1 += 1
    if (len2 < len1):
        while (len2 < len1):
            number2 = '0' + number2
            len2 += 1
    i = len2
    while (i > 0):
        if (int(number1[i-1])+int(number2[i-1])+carry > 9):
            carry = 1
            carries += 1
        else:
            carry = 0
        i -= 1
    return carries


def main():
    """
    Call other functions
    None -> None
    """
    number1, number2 = my_input()
    sum_fun(number1, number2)
    print("Number of carries:", count_carry(number1, number2))


main()
