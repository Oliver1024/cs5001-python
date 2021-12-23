def print_cube(m):
    """
    Using for loop to print each edge of the cube
    Number -> None
    """
    # Assign values to variable and constant
    HALF_NUM = 2
    n = int(m / HALF_NUM)
    print(" " * (n + 1) + "+" + "-" * (m * HALF_NUM) + "+")

    for i in range(n):
        print(" " * (n - i) + "/" + " " * (HALF_NUM * m) + "/" + " " * i + "|")
    print("+" + "-" * (HALF_NUM * m) + "+" + " " * n + "|")
    for i in range(m):
        if i < m - (n + 1):
            print("|" + " " * (HALF_NUM * m) + "|" + " " * n + "|")
        elif i > m - (n + 1):
            print("|" + " " * (HALF_NUM * m) + "|" +
                  " " * (n - (i - n + 1)) + "/")
        elif i == m - (n + 1):
            print("|" + " " * (HALF_NUM * m) + "|" + " " * n + "+")
    print("+" + "-" * (HALF_NUM * m) + "+")


def main():
    """
    Call print_cube() function
    None -> None
    """
    EVEN_NUM = 2  # Assign value to constant name
    input_num = int(input("Input cube size (multiple of 2): "))
    while input_num % EVEN_NUM != 0:
        input_num = int(input("Input cube size (multiple of 2): "))
    print_cube(input_num)


main()
