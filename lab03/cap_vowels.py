# Kejian Tong
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab03

# Assign vowels letter to variable
vowels = ['a', 'e', 'i', 'o', 'u']
# Prompt users to input strings
my_str = (input("Users input some capitalized strings: ")).lower()


def main():
    for letter in my_str:
        if letter in vowels:
            letter_up = letter.upper()
            print(letter_up, end='')
        else:
            b = letter.lower()
            print(b, end='')
    print()


main()
