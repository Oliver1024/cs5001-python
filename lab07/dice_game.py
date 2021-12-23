from game_controller import GameController


def main():
    """
    Call other function
    None -> None
    """
    print("--------------------------------")
    print("Welcome to street craps!\n", "\nRules:")
    MESSAGE1 = "If you roll 7 or 11 on your first roll, you win.\n"
    MESSAGE2 = "If you roll 2, 3, or 12 on your first role, you lose.\n"
    MESSAGE3 = "If you roll anything else, that's your 'point', and\n"
    MESSAGE4 = "you keep rolling until you either roll your point\n"
    MESSAGE5 = "again(win) or roll a 7 (lose)\n"
    print(MESSAGE1 + MESSAGE2 + MESSAGE3 + MESSAGE4 + MESSAGE5 + "\n")

    gc = GameController()
    gc.start_play()


main()
