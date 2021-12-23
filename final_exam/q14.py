def count(n):
    if n <= 0:
        print("Let's go!")
    else:
        count(n-3)
        print(n)
count(5)