# The define main function and use while to determine numbers from input
def main():
    n = int(input("Please input the value: "))
    while n % 2 == 0 or n < 3:
        n = int(input("input a different (odd) number: "))

    height = int((n + 1) / 2)
    left_space = int((n - 1) / 2)

    """
    Use for loop to judge the relationship between whitespace
    and "\" "/" line by line and print
    """
    for i in range(1, height+1):
        if i == 1:
            for j in range(left_space):
                print(" ", end="")
            print("*", end="\n")
        elif i == height:
            all_side = "/" + "_" * (n - 2) + "\\"
            print(all_side)
        else:
            both_side = (" " * int(((n+1)/2)-i) + "/" + " " * ((i-2)*2+1)+"\\")
            print(both_side)


main()
