import sys


def main():
    # Assign initial none values to the list
    fib_lst = [0, 1]
    # Assign initial value to variables
    n = int(sys.argv[1])

    # Get the Fibonacci numbers
    if n > 2:
        for i in range(2, n):
            next_num = fib_lst[i - 1] + fib_lst[i - 2]
            fib_lst.append(next_num)

    # Print the results
    print("Fibonacci numbers are:", fib_lst)


main()
