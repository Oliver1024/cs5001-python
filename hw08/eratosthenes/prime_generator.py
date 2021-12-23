class PrimeGenerator:
    """
    A class that can generate prime numbers
    """
    def __init__(self):
        """
        Initialize the class
        """
        self.primes = []  # primes stored in a list
        self.composite_set = set()  # composites stored in a set
        self.INTERVAL = 2

    def primes_to_max(self, num):
        """
        Get prime numbers
        Number -> Number
        """
        for i in range(self.INTERVAL, num):
            if i not in self.composite_set:
                self.primes.append(i)

                for j in range(i + self.INTERVAL, num, self.INTERVAL):
                    if j not in self.composite_set:
                        self.composite_set.add(j)
            self.INTERVAL += 1
        return self.primes
