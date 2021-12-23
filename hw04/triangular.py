'''
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw04
Name: Kejian Tong
'''
import sys


# Define my main function
def main():
    num = 0
    n = int(sys.argv[1])
    # Asiign none list to lst
    lst = []
    # From 0 to n, take out the triangle numbers one by one
    for i in range(0, n):
        num += i
        lst.append(num)  # Append each num to lst

    print("The Triangular number are:", lst)  # Print the lst


main()
