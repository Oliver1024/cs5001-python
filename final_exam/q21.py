def spam(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return  spam(m - 1, 1)
    elif m > 0 and n > 0:
        return spam(m -1, spam(m, n - 1))

result = spam(1, 0)
print(result)