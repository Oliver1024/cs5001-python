import math


def main():
    # Prompt the user to enter an angle value and assign it to cosnum and sinum
    num = int(input("Enter an angle: "))

    # Compute the values of cosine and sine 
    out_cosnum = math.cos(math.radians(num))
    out_sinnum = math.sin(math.radians(num))

    # Print the results
    print("The cosine of", num, "is", out_cosnum)
    print("The sine of", num, "is", out_sinnum)
    

main()
    
