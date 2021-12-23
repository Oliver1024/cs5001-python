from team import Team
from bench import Bench


def main():
    """
    Call other functions
    """
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            # TODO: call a function that calls
            # the appropriate method on the team
            # object to cut the player (you need
            # to write the function below)
            do_cut_player(the_team, the_bench)

        elif command == "show bench":
            # TODO: call a function to call the necessary
            # bench method to show the names of the players
            # who are currently on the bench.
            do_show_bench(the_bench)

        else:
            do_not_understand()


def do_set_team_name(team):
    """
    Call other function to set team's name
    """
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    """
    Call other function to show team information
    """
    # TODO: call the method on the team object that
    # displays the roster
    team.do_show_team_roster()


def do_check_position_filled(team):
    """
    Check position information in team
    """
    position = input("What position are you checking for?\n")
    # TODO: call the method on the team object that determines
    # whether a given position has at least one player filling it,
    # then print the appropriate message:
    # "Yes, the", position, "position is filled"
    # or
    # "No, the", position, "position is not filled"
    if team.is_position_filled(position):
        print("Yes, the", position, "position is filled")
    else:
        print("No, the", position, "position is not filled")


def do_add_player_to_team(team):
    """
    Call other functions to add players to team
    """
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    player_number = varify_number_input(player_number, team)
    player_position = input("What's " + player_name + "'s position?\n")
    player_position = verify_position_input(player_position)
    # TODO: call the method on team that creates a new player and
    # adds the player to the team.
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    """
    Call other function to send player to team
    """
    name = input("Who do you want to send to the bench?\n")
    # TODO: make sure that the player is actually on the team first,
    # and then call a method on the bench object to place the player
    # "on the bench". If this is accomplished successfully, print
    # "Sent", name, "to bench."
    # otherwise print
    # name, "isn't on the team."

    # check if player in team
    in_team = check_player_in_team(name, team)
    if in_team:
        bench.send_to_bench(name)
        print("Sent", name, "to bench")
    else:
        print(name, "isn't on the team")


def do_get_player_from_bench(bench):
    """
    Call other function to get player from bench
    """
    # TODO: get the best-rested player by name from the bench
    # (i.e. the player who has been on the bench longest). Print to
    # the screen the name of the player who was retrieved from the
    # bench. If the bench is empty, print to the screen that the
    # bench is empty.
    player = bench.get_from_bench()
    if player:
        print(f"you get {player} from bench.")
    else:
        print("The bench is empty.")

# TODO: write a function that calls the appropriate method on the team
# object to cut the player


def do_cut_player(team, bench):
    """
    Call other function to cut players
    """
    if len(team.players) == 0:
        print("The team currently has no players")
        return
    player_name = input("Who do you want to cut?\n")
    if player_name in bench.bench:
        print("This player is on bench and forbid cutting a benched player")
        return
    for player in team.players:
        if player_name == player.player_name:
            team.cut_player(player_name)
            return
    print("This player is not on the team")

# TODO: write a function to call the necessary method to show the
# names of the players who are currently on the bench.


def do_show_bench(bench):
    """
    Call other function to show player information on bench
    """
    bench.show_player_on_beach()


def do_not_understand():
    """
    Print information when input invalid command
    """
    print("I didn't understand that command")


def check_player_in_team(name, team):
    """
    Check whether a player in team
    """
    for player in team.players:
        if name == player.player_name:
            return True
    return False


def enforce_input_player_number(player_number):
    """
    Enforce users input a number
    """
    try:
        player_number = int(player_number)
        return True
    except ValueError:
        return False


def check_input_player_number(player_number, team):
    """
    Check whether the input number exists in team
    """
    for num in team.players:
        if player_number == num.player_number:
            return False
    return True


def varify_number_input(player_number, team):
    """
    Varify the input number and return a valid number
    """
    is_input_correct = False
    while not is_input_correct:
        if not enforce_input_player_number(player_number):
            player_number = input("Please input a integer number:\n")
        elif not check_input_player_number(player_number, team):
            player_number = input(
                "This number has existed in team, Please try another:\n")
        else:
            is_input_correct = True

    return player_number


def enfoce_input_required_position(player_position):
    """
    Check input position's name
    """
    roster_position = {"catcher", "corner", "sniper", "thrower"}
    for position in roster_position:
        if player_position not in roster_position:
            return False
        else:
            return True


def verify_position_input(player_position):
    """
    Varify the input position name and return a valid name
    """
    is_input_correct = False
    while not is_input_correct:
        if not enfoce_input_required_position(player_position):
            player_position = input("Please input a required position name:\n")
        else:
            is_input_correct = True
    return player_position


main()
