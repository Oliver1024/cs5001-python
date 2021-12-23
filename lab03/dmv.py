import random

# Assign some variables
WELCOME = str("Welcome to the DMV (estimated"
              + "wait time is 3 hours)")

print(str("Please enter your first, middle,and last name: "))
full_name = input()

print("Enter date of birth (MM/DD/YY): ")
dob = input()

sep_line = "----------------------------"
NAME_LIC = "Washington Driver License"

print(sep_line)
print(NAME_LIC)

# Print the result
print(WELCOME)

# Define my main function


def main():
    # Produce a 7-digit random number
    drive_license = ''
    for i in range(7):
        num = random.randint(0, 9)
        drive_license += str(num)

    # Find last anme first name
    name_break = full_name.rfind(' ')
    last_name = full_name[name_break + 1:]
    first_name = full_name[: name_break]

    # Using rfind() replace year of birth
    date_break = dob.rfind('/')
    last_line = dob[: date_break]
    my_exp = dob.replace(dob[date_break + 1:], '21')

    # Print the final results
    print("DL", drive_license)
    print("LN", last_name)
    print("FN", first_name)
    print("DOB", dob)
    print("EXP", my_exp)


main()
