# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw06
# Name: Kejian Tong

def triangular_number():
    """
    Using while and for loop to get triangular numbers and
    append these numbers to a list and then print them finally
    None -> None
    """
    message = ""
    message = input("Enter a number, or enter 'done': ")
    output_list = []

    while message != "done":
        num = 0
        triangle_list = []
        n = int(message)
        for i in range(1, n + 1):
            num += i
            triangle_list.append(num)
        output = print("The triangular number for",
                       message, "is", triangle_list[n-1])
        message = input("Enter a number, or enter 'done': ")
        output_list.append(triangle_list[n-1])
    print(output_list)


def main():
    """
    Call the function
    None -> None
    """
    triangular_number()


main()
