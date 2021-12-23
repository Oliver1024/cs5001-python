class Player:
    """A class representing a dodgeball player"""
    # TODO: Write a constructor (__init__() method) that
    # will take the necessary values, set them to
    # the player object's attributes, and create the
    # new instance of player. Like all methods, its first
    # parameter must be `self`. The remaining parameters should
    # receive whatever pieces of data are relevant to creating
    # a new Player object.

    def __init__(self, player_name, player_number, player_position):
        """
        Initialize the Player attributes
        """
        self.player_name = player_name
        self.player_number = player_number
        self.player_position = player_position

    def __str__(self):
        """
        Provide a string represntation of a player object
        """
        return (f"{self.player_number}\t{self.player_name}\t \
                {self.player_position}")
