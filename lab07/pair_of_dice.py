from die import Die


class PairOfDice:
    """
    A class representing a pair of dice
    """
    def __init__(self):
        """
        Initialize the PairOfDice
        """
        self.dice1 = Die()
        self.dice2 = Die()

    def roll_dice(self):
        """
        Roll a pair of dice
        """
        self.dice1.roll()
        self.dice2.roll()

    def current_value(self):
        """
        Get the sum of a pair of dice after a roll
        None -> Number
        """
        return self.dice1.current_value + self.dice2.current_value
