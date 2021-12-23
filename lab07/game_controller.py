from pair_of_dice import PairOfDice


class GameController:
    """
    A class that controls how to roll a dice
    """

    def __init__(self):
        """
        Initialize the GameController
        """
        self.point = None
        self.pod = PairOfDice()
        self.GAME_OVER = False
        self.sum = None
        self.WIN_LIST = [7, 11]
        self.LOSE_LIST = [2, 3, 12]
        self.LOSE_POINT = 7

    def start_play(self):
        """
        Starting to roll the dice
        """
        input("Press enter to roll the dice...")
        print("")
        self.pod.roll_dice()
        self.sum = self.pod.current_value()
        self.point = self.sum
        self.compare_score()

        while not self.GAME_OVER:
            input("Press enter to roll the dice...")
            print("")
            self.pod.roll_dice()
            self.sum = self.pod.current_value()
            self.compare_other()

    def compare_score(self):
        """
        Compare the result of first roll whether win or lose
        """

        if self.sum in self.WIN_LIST:
            print(f"You rolled {self.sum}. You win!\n")
            self.GAME_OVER = True
        elif self.sum in self.LOSE_LIST:
            print(f"You rolled {self.sum}. You lose.\n")
            self.GAME_OVER = True
        else:
            print(f"Your point is {self.point}")

    def compare_other(self):
        """
        Compare the results of other times whether win or lose
        """

        if self.sum == self.LOSE_POINT:
            print(f"You rolled {self.sum}. You lose.\n")
            self.GAME_OVER = True
        elif self.sum == self.point:
            print(f"You rolled {self.sum}. You win!\n")
            self.GAME_OVER = True
        else:
            print(f"Your rolled {self.sum}")
