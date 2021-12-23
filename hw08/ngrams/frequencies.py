from text_cleaner import TextCleaner


class NgramFrequencies:
    """
    A class that producing Ngram frequencies
    """

    def __init__(self, word_number):
        """
        Initialize the Class of NgramFrequencies
        """
        self.char_counts = {}
        self.total_count = 0
        self.tc = TextCleaner()
        self.ngram_num = 0
        self.each_line = ""
        self.token_each_line = []
        self.word_number = word_number
        self.round_num = 3

    def add_item(self, line):
        """
        Takes an n-gram and increments its count in the dictionary
        String -> Dictionary
        """
        self.token_each_line = self.tc.pre_process_text(line)
        self.ngram_num = self.word_number - 1
        self.tmp_words = []

        for i in range(0, len(self.token_each_line) - self.ngram_num):
            for j in range(i, i + self.word_number):
                self.tmp_words.append(self.token_each_line[j])
            tmp_str = "_".join(self.tmp_words)
            self.tmp_words = []
            self.total_count += 1
            if tmp_str in self.char_counts.keys():
                self.char_counts[tmp_str] += 1
            else:
                self.char_counts[tmp_str] = 1
        return self.char_counts

    def top_n_counts(self, N):
        """
        returns list of items sorted on the count, with the most frequent first
        Number -> Number
        """
        return sorted(
            self.char_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[0:N]

    def top_n_freqs(self, N):
        """
        returns a similar list as above, but with frequencies instead of counts
        Number -> Tuple
        """
        return [(word, self.frequency(word))
                for (word, _) in self.top_n_counts(N)]

    def frequency(self, word):
        """
        takes an item and returns its frequency
        String -> Number
        """
        return round(self.char_counts[word] / self.total_count, self.round_num)
