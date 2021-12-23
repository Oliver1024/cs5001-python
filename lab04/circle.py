import math
import sys


def main():
    """Define a function, using the Pythagorean theorem, in judging
       the distance between the coordinates i, j and the center of the circle
    """
    radius = int(sys.argv[1])
    for i in range(2*radius):
        for j in range(2*radius):
            # Calculate the distance of the coordinates
            distance = math.sqrt(abs(j - radius)**2 + abs(i - radius)**2)
            # Compare the coordinate distance with radius
            if distance < radius:
                print('o', end='')
            else:
                print(' ', end='')
        print()


main()
