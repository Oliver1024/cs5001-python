# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab08
# Name: Kejian Tong

import sys
from data_analysis import DataAnalysis


def main(file_name):
    """
    Call other functions
    """
    FREQS_NUM = 10
    try:
        data = DataAnalysis(file_name)
    except Exception:
        print("Can't find", file_name)
        return
    # Report top ten languages by frequency
    print("Languages:")
    print_output(data.top_n_lang_freqs(FREQS_NUM))

    # Report top ten country (2 letter) top
    # level domains by frequency
    print("Top level country domains:")
    print_output(data.top_n_country_tlds_freqs(FREQS_NUM))


def print_output(collection):
    """
    Format the printed results
    """
    ROUND_NUM = 3
    for item in collection:
        print(item[0]+":  \t", round(item[1], ROUND_NUM))


main(sys.argv[1])
