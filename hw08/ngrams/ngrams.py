# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw08/ngrams
# Kejian Tong

import sys
from frequencies import NgramFrequencies


def main(file_name):
    """
    Call other functions
    """
    n = 10
    unigram = NgramFrequencies(1)
    bigram = NgramFrequencies(2)
    trigram = NgramFrequencies(3)

    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return

    while True:
        per_line = f.readline()
        if not per_line:
            break
        unigram.add_item(per_line)
        bigram.add_item(per_line)
        trigram.add_item(per_line)

    def print_output(collection):
        """
        A common print_output function
        """
        for item in collection:
            print("   ", item)

    # Print the final results
    print("Top 10 unigrams:")
    print_output(unigram.top_n_freqs(n))
    print("Top 10 bigrams:")
    print_output(bigram.top_n_freqs(n))
    print("Top 10 trigrams:")
    print_output(trigram.top_n_freqs(n))


main(sys.argv[1])
