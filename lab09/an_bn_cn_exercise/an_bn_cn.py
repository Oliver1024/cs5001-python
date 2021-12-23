import sys
sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # nopep8
# from stack_linked_list import Stack  # nopep8


class AnBnCn:
    """
    Class for evaluating strings of n A's followed by n B's and
    strings of n B's followed by n C's
    """

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def accept(self, in_string):
        """
        Takes a string and returns a boolean
        indicating whether the string matches the pattern
        """
        expect_a = True
        expect_b = True
        for ch in in_string.lower():
            # If we see an expected a, put it in the stack.
            if ch == "a":
                if expect_a:
                    self.stack_1.push(ch)
                else:
                    # unexpected a -> fail
                    return False
            elif ch == "b":
                if self.stack_1.is_empty():
                    return False
                else:
                    if expect_a:
                        expect_a = False
                    self.stack_2.push(ch)
                    self.stack_1.pop()
            elif ch == "c":
                if self.stack_2.is_empty():
                    return False
                else:
                    if expect_b:
                        expect_b = False
                    self.stack_2.pop()

        if self.stack_1.is_empty() and self.stack_2.is_empty():
            return True
        return False

    def clear(self):
        """
        Clear the stack at the end of each checker
        """
        self.stack_1 = Stack()
        self.stack_2 = Stack()
