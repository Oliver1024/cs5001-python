"""
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab04
Name: Kejian Tong
"""
# Get values from user input
symbol = input("Prompt user input the symbol: ")
width = int(input("Prompt user input the width: "))
height = int(input("Prompt user input the height: "))
exception = "the value is too small"


# Define a main function to achieve logical judgement
def main():
    if height >= 2 and width >= 2:
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if i == 1 or i == height or j == 1 or j == width:
                    print(end=symbol)
                else:
                    print(end=' ')
            print()
    else:
        print(exception)


main()
