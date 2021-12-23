# Assign initial values to variables
N = 3
matrix_value = 15


def my_input():
    """It will get 3 numbers from the user
    Returns:
      integer : num1, num2, num3
    """
    num1 = int(input("Enter a magic number: \n"))
    num2 = int(input())
    num3 = int(input())
    return num1, num2, num3


def my_lst():
    """ Generate three list
    Returns:
        list : lst1, lst2, lst3
    """
    num1, num2, num3 = my_input()
    lst1 = [int(i) for i in str(num1)]
    lst2 = [int(i) for i in str(num2)]
    lst3 = [int(i) for i in str(num3)]
    return [lst1, lst2, lst3]


# Define my row function to determine the sum of each row
def my_row(magic_num):
    for i in range(N):
        sum_row = sum(magic_num[i])
        if sum_row != matrix_value:
            return False
    return True


# Define the column function to determine the sum of each column
def my_col(magic_num):
    for i in range(N):
        sum_col = 0
        for j in range(N):
            sum_col += magic_num[j][i]
        if sum_col != matrix_value:
            return False
    return True


# Define a function to compute the sum of diaginal values
def my_dia(magic_num):
    # Assign initial values
    sum_dia1 = 0
    sum_dia2 = 0
    sum_dia1 = sum([magic_num[i][i] for i in range(N)])
    sum_dia2 = sum([magic_num[i][N-i-1] for i in range(N)])

    if sum_dia1 == matrix_value and sum_dia2 == matrix_value:
        return True
    else:
        return False


# Define my main function
def main():
    magic_num = my_lst()
    if my_row(magic_num) and my_col(magic_num) \
       and my_dia(magic_num):
        print("This is a magic square!")
    else:
        print("Not a magic square!")


main()
