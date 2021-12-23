import random


def main():
    # Assign values to constants
    MSG0 = "You guessed"
    MSG1 = "Your guess is scalding hot"
    MSG2 = "Your guess is extremely warm"
    MSG3 = "Your guess is very warm"
    MSG5 = "Your guess is warm"
    MSG8 = "Your guess is cold"
    MSG13 = "Your guess is very cold"
    MSG20 = "Your guess is extremely cold"
    MSG = "Your guess is icy freezing miserably cold"
    TOTAL = "Congratulations. You figured it out in"
    print("Welcome to the Guessing Game!")
    print("I picked a number between 1 and 50. Try and guess!")

    # Define a integer random between 1 and 50
    num = random.randint(1, 50)
    guess = int(input())
    print(MSG0, guess)

    # My while loop logical judgement
    count = 1
    while (num != guess):
        if abs(guess - num) == 1:
            print(MSG1)
            guess = int(input())
        elif abs(guess - num) == 2:
            print(MSG2)
            guess = int(input())
        elif abs(guess - num) == 3:
            print(MSG3)
            guess = int(input())
        elif abs(guess - num) <= 5:
            print(MSG5)
            guess = int(input())
        elif abs(guess - num) <= 8:
            print(MSG8)
            guess = int(input())
        elif abs(guess - num) <= 13:
            print(MSG13)
            guess = int(input())
        elif abs(guess - num <= 20):
            print(MSG20)
            guess = int(input())
        else:
            print(MSG)
            guess = int(input())
        count += 1

    # Print the total counts
    print(TOTAL, count, "tries")


main()
