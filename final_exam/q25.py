def count_down_by_two(n):
    if n<=0:
        print("ok")
    else:
        count_down_by_two(n-2)
        print(n)
count_down_by_two(5)