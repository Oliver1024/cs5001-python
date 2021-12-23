# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab09/an_bn_cn_exercise
# Kejian Tong

from an_bn_cn import AnBnCn


def main():
    """
    Call other function
    """
    an_bn_cn = AnBnCn()
    line = input("Input a string:\n")
    if an_bn_cn.accept(line):
        print("This string is accepted")
    else:
        print("This string is rejected")


main()
