
class Stack:
    """A stack class implemented with a Python list"""
    def __init__(self):
        """
        Initializes stack
        """
        # we can use a python list as the underlying
        # representation, but this is an implementational
        # choice. We do not have to use a list, we just need
        # to make sure we have an ordered collection and are
        # able to access the first and the last.
        self.items = []

    def __str__(self):
        """
        Provides string for stack
        Self -> String
        """
        return self.items.__str__()

    def push(self, item):
        """
        Pushes an item onto the stack
        Self Object -> None
        """
        self.items.append(item)

    def pop(self):
        """
        Pops an item from the stack
        Self -> Object
        """
        return self.items.pop()

    def peek(self):
        """
        Checks the next item on the stack
        Self -> Object
        """
        return self.items[-1]

    def is_empty(self):
        """
        Tells whether the stack is empty
        Self -> Boolean
        """
        if len(self.items) == 0:
            return True
        else:
            return False
