"""
This program created by Kejian Tong, is mainly through a main function,
after the user enters the parameters, the user is
given the recommended username and 3 optional passwords.
The main function is mainly realized by concatenating some strings
and using methods such as replace and join.
"""
import random


def main():
    print("Welcome to the username and password generator!")
    ft_name = input("Please enter your first name: ")
    lt_name = input("Please enter your last name: ")
    fv_word = input("Please enter your favorite word: ")
    N = 99  # Replace magic number
    print()

    # Generate username
    username = ''
    random_num1 = random.randint(0, N)
    random_num2 = random.randint(0, N)
    ft_name = ft_name.capitalize()
    len_lt = len(lt_name)

    """
    Determine the relationship between the length of firstname
    and number 7 to decide whether to use asterisk to fill in and
    use string slicing to take letters.
    """
    if len(lt_name) >= 7:
        username = (ft_name[0] + lt_name[0:7]).lower() + str(random_num1)
        print("Thanks", ft_name, ",", "your user name is", username, "\n")
    else:
        username = (ft_name[0] + lt_name[0:len_lt]).lower() + \
            (7 - len_lt) * "*" + str(random_num2)
        print("Thanks", ft_name, ",", "your user name is", username, "\n")

    print("Here are three suggested passwords for you to consider: \n")

    """
    Use the replace method to replace specific letters. Use string index
    and upper and lower methods to generate password. Use random to take out
    the random string part of the name and favorite word, then construct a
    list, and finally use random.shuffle and join to generate the 3rd password.
    """
    # Generate password1
    password1 = ft_name + str(random.randint(0, N)) + lt_name

    password1 = password1.replace("a", "@")
    password1 = password1.replace("l", "1")
    password1 = password1.replace("s", "$")
    password1 = password1.replace("o", "0")

    print("Password 1:", password1)

    # Generate password2
    password2 = ft_name[0].lower() + ft_name[-1].upper() \
        + lt_name[0].lower() + lt_name[-1].upper() \
        + fv_word[0].lower() + fv_word[-1].upper()

    print("Password 2:", password2)

    # Generate password3
    ft_len = random.randint(1, len(ft_name))
    fv_len = random.randint(1, len(fv_word))
    lt_len = random.randint(1, len(lt_name))
    # Get different strings assigned to variables
    p1 = ft_name[0:ft_len]
    p2 = fv_word[0:fv_len]
    p3 = lt_name[0:lt_len]
    # Generate a list named password3
    password3 = [p1, p2, p3]
    # Get a random string from the list
    random.shuffle(password3)

    password3 = "".join(password3)
    print("Password 3:", password3)


main()
