from player import Player
from bench import Bench
import re


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.

    def __init__(self):
        """
        Initialize the Team
        """
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        """
        Set team's name
        """
        # TODO: set the team name
        for char in name:
            if((re.match(r"\W", char) or char == "_") and char != " "):
                print("Team name should not include special symbols")
                return
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        """
        Add players to team
        """
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        new_player = Player(player_name, player_number, player_position)

        # an instance of class = object
        self.players.append(new_player)

    def cut_player(self, player_name):
        """
        Cut players from team
        """
        # TODO: Remove the player with the name player_name
        # from the players list.
        if len(self.players) > 0:
            for i in range(len(self.players)):
                if self.players[i].player_name == player_name:
                    del self.players[i]
                    return
        else:
            print("There is no players to cut")

    def is_position_filled(self, position):
        """
        Check whether a position is already in team
        """
        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        for item in self.players:
            if item.player_position == position:
                return True
        return False

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:

    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper

    def do_show_team_roster(self):
        """
        Show current team information in roster
        """
        header = "The lineup for " + self.name + " is:"
        if len(self.players) > 0:
            print(header, end="\n")
            for p in self.players:
                print(p.__str__())
        else:
            print(header, end="\n")
            print("The team currently has no players")
