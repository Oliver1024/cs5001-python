def foo(n):
    if n < 1:
        return -1
    else:
        return n * foo(n-3)

print(foo(7))