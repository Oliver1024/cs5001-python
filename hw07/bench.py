class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        """
        Initialize the Bench
        """
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.bench = []

    def send_to_bench(self, player_name):
        """
        Send players to bench
        """
        # TODO: Put the player "onto the bench"
        self.bench.insert(0, player_name)

    def check_bench_empty(self):
        """
        Check the bench whether is empty or not
        """
        if len(self.bench) > 0:
            return False
        else:
            return True

    def get_from_bench(self):
        """
        Get players from bench
        """
        # TODO: Return the name of the player who has
        # been on the bench
        if not self.check_bench_empty():
            return self.bench.pop()
        else:
            return False

    # TODO: Write the function that will display the
    # current list of players on the bench

    def show_player_on_beach(self):
        """
        Show players on the bench
        """
        if not self.check_bench_empty():
            print("The bench currently includes:", end='\n')
            for item in range(len(self.bench)):
                print(self.bench[item])
        else:
            print("The bench is empty.")
    # TODO: Write any other methods that might be used
    # by the methods above.
