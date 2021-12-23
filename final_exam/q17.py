from stack_python_list import Stack


def mystery(s, values):
    for val in values:
        s.push(val)  # Line A
    n = 20
    for i in range(4):
        n += s.pop()  # Lline B
    for i in range(2):
        n -= s.pop()  # Line C
    return n


def main():
    values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    stack = Stack()
    print(mystery(stack, values)) 


main()