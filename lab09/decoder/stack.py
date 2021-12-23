
class Stack:
    """A stack class"""
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
        if self.items:
            return self.items.pop()
        else:
            return ""

    def peek(self):
        """
        Get the last item on the stack
        Self -> Object
        """
        if self.items:
            return self.items[-1]
        else:
            return None
