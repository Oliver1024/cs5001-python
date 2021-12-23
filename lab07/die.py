# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab07
# Name: Kejian Tong

import random


class Die:
    """
    A class representing a dice
    """

    def __init__(self):
        """
        Initialize the Die
        """
        self.MIN_VALUE = 1
        self.MAX_VALUE = 6
        self.current_value = random.randint(self.MIN_VALUE, self.MAX_VALUE)

    def roll(self):
        """
        Define the random value when rolling a dice
        """
        self.current_value = random.randint(self.MIN_VALUE, self.MAX_VALUE)
