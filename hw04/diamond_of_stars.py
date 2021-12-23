import sys


def main():
    height = int(sys.argv[1])
    upper_n = height // 2 + 1
    low_n = height - upper_n
    # The input value is odd and compute stars and space
    if height % 2 != 0:
        # Print the upper part of the diamond first
        for i in range(1, upper_n + 1):
            print(' ' * (low_n - (i - 1)) + "*" * (2 * i - 1))
        # Print the lower part of the diamond
        for j in range(1, low_n + 1):
            print(" " * j + "*" * (height - 2 * j))
    else:
        # The input value is even
        for i in range(1, upper_n):
            print((low_n - (i - 1)) * ' ' + (2 * i - 1) * '*')
        for j in range(1, low_n + 2):
            print((j - 1) * " " + (2 * (upper_n - j) - 1) * '*')


main()
