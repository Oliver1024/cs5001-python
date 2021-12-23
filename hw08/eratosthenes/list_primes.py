# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw08/eratosthenes
# Name: Kejian Tong

from prime_generator import PrimeGenerator


def main():
    """
    Call other function
    """
    prime_generator = PrimeGenerator()
    num = int(input("Please input a max number: "))
    print("List of prime numbers:")
    primes = prime_generator.primes_to_max(num)
    print(primes)


main()
