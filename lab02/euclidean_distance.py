import math


def main():
    # Prompt the user to enter four numerical values
    x1 = input("Please input x1 coordinate: ")
    y1 = input("Please input y1 coordinate: ")
    x2 = input("Please input x2 coordinate: ")
    y2 = input("Please input y2 coordinate: ")

    # Assign the sum of squares of the differences to the variables dist1 and dist2
    dist1 = (int(x1) - int(y1))**2
    dist2 = (int(x2) - int(y2))**2

    # Calculate the euclidean distance and the result is kept 2 decimal
    eucldist = round(math.sqrt(dist1 + dist2), 2)

    # Print the result
    print("This is the euclidean distance:", eucldist)


main()