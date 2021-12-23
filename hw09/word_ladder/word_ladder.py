from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        """
        Initialize the class
        """
        num_min = 97
        num_max = 123
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist
        self.queue = Queue()
        init_stack = Stack()
        init_stack.push(self.w1)
        self.queue.enqueue(init_stack)
        self.exist = {self.w1}
        self.alphabet = [chr(a) for a in range(num_min, num_max)]

    def make_ladder(self):
        """
        Find the shortest way to get the target
        Self -> Stack(String)
        """

        while not self.queue.isEmpty():  # check if self.queue is not empty
            stack = self.queue.dequeue()  # a stack to store queue list
            top_word = stack.peek()  # get the last word from stack
            for item in range(len(top_word)):
                for char in self.alphabet:
                    # replace char using the letter
                    temp_word = self.string_replace(top_word, item, char)
                    if temp_word == self.w2:
                        stack.push(temp_word)
                        return stack
                    elif temp_word in self.wordlist and temp_word \
                            not in self.exist:
                        new_stack = stack.copy()
                        new_stack.push(temp_word)
                        self.queue.enqueue(new_stack)
                        self.exist.add(temp_word)
        return None

    def string_replace(self, string, index, repl_letter):
        """
        Replace letters of words
        Self, String, Number, String -> String
        """
        return (string[0: index] + repl_letter + string[index+1:])
