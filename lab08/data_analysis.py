import re
import pandas as pd


class DataAnalysis:
    """
    A class doing the data analysis
    """
    def __init__(self, file):
        """
        Initialize the DataAnalysis
        """
        # TODO: set up the necessary instance variables
        # self.file = file
        self.count = 0
        self.top_lang = {}
        self.top_country = {}
        self.data_file = self.read_data(file)
        self.FIRST_VALUE = 1

    def read_data(self, file_name):
        """
        Read file content from csv file
        """
        # TODO: read the data and get the counts

        self.data_file = pd.read_csv(file_name)
        self.count = self.data_file.shape[0]
        return self.data_file
        # The shape attribute of pandas.DataFrame stores the number
        # of rows and columns as a tuple (number of rows, number of columns).

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.

    def top_n_lang_freqs(self, N):
        """
        Get top N frequencey of languages and reutrn list of tuple
        """
        lst = list(self.data_file['language'])
        for line in lst:
            if line in self.top_lang.keys():
                self.top_lang[line] += 1
            else:
                self.top_lang[line] = 1

        list_tuple = [(lst, self.top_lang[lst]/self.count)
                      for lst in self.top_lang.keys()]
        list_tuple_sort = sorted(
            list_tuple, key=lambda x: x[self.FIRST_VALUE], reverse=True)
        return list_tuple_sort[0:N]

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.

    def top_n_country_tlds_freqs(self, N):
        """
        Get top N frequencey of countries and reutrn list of tuple
        """
        lst = list(self.data_file['email'])
        for email in lst:
            item = re.search("\\.[a-zA-Z]{2}\\Z", email)
            if item:
                domain = item.group().replace(".", "")
                if domain in self.top_country.keys():
                    self.top_country[domain] += 1
                else:
                    self.top_country[domain] = 1

        list_tuple = [(lst, self.top_country[lst]/self.count)
                      for lst in self.top_country.keys()]
        list_tuple_sort = sorted(
            list_tuple, key=lambda x: x[self.FIRST_VALUE], reverse=True)
        return list_tuple_sort[0:N]
