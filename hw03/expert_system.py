# Kejian Tong
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw03

# Define some diagnostic questions and Yes or No prompt
q1 = "Are you coughing?" + " Yes or No: "
q2 = "Do you have a headache?" + " Yes or No: "
q3 = str("Are you experiencing any of the following:"
         + "when bending your head forward,"
         + "nausea or vomiting, bright light hurting,"
         + "your eyes drowsiness or confusion?"
         + " Yes or No: ")
q4 = "Are you vomiting or had diarrhea?" + " Yes or No: "
q5 = str("Are you short of breath or wheezing or"
         + "coughing up phelgm?" + " Yes or No: ")
q6 = str("Do you have aching bones or aching joints?"
         + " Yes or No: ")
q7 = "Do you have a rash?" + " Yes or No: "
q8 = "Do you have a sore throat?" + " Yes or No: "
q9 = str("Do you have back pain just above the waist"
         + "with chills and fever?" + " Yes or No: ")
q10 = str("Do you have pain urinating or are urinating more often?"
          + " Yes or No: ")
q11 = str("Have you spent the day in the sun or in hot conditions?"
          + " Yes or No: ")

# Define some possibile symptoms
s1 = "Possibilities include menigitis."
s2 = "Possibilities include digestive tract infection."
s3 = "Possibilities include pneumonia or infection of airways."
s4 = "Possibilities include viral infection."
s5 = "Insufficient information to list possibilities."
s6 = "Possibilitiese include a throat infection."
s7 = "Possibilities include kidney infection."
s8 = "Possibilities include a urinary tract infection."
s9 = "Possibilities sunstroke or heat exhaustion."

# Define a function to replace repeated elif/else code


def my_fun():
    choice = input(q6).lower()
    if choice == 'yes':
        print(s4)
    else:
        choice = input(q7).lower()
        if choice == 'yes':
            print(s5)
        else:
            choice = input(q8).lower()
            if choice == 'yes':
                print(s6)
            else:
                choice = input(q9).lower()
                if choice == 'yes':
                    print(s7)
                else:
                    choice = input(q10).lower()
                    if choice == 'yes':
                        print(s8)
                    else:
                        choice = input(q11).lower()
                        if choice == 'yes':
                            print(s9)
                        else:
                            print(s5)


# Define the main function to execute the entire logical judgment
def main():
    # The diagnostic control logic
    choice = input(q1).lower()
    if choice == 'no':
        choice = input(q2).lower()
        if choice == 'yes':
            choice = input(q3).lower()
            if choice == 'no':
                choice = input(q4).lower()
                if choice == 'yes':
                    print(s2)
                else:
                    my_fun()
            else:
                print(s1)
        else:
            my_fun()
    else:
        choice = input(q5).lower()
        if choice == 'yes':
            print(s3)
        else:
            choice = input(q2).lower()
            if choice == 'yes':
                print(s4)
            else:
                my_fun()


main()
