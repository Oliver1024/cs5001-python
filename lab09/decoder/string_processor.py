from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        """
        Initializes class
        """
        self.lst = []
        self.asterisk = "*"
        self.caret = "^"
        self.stack = Stack()

    def process_string(self, in_string):
        """
        Process the in_put string
        String -> String
        """
        for ch in in_string:
            if ch == self.asterisk:
                self.lst.append(self.stack.pop())
            elif ch == self.caret:
                self.lst.append(self.stack.pop())
                self.lst.append(self.stack.pop())
            else:
                self.stack.push(ch)
        return "".join(self.lst)
