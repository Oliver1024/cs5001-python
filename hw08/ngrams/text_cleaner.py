import re


class TextCleaner:
    """
    A class represents the TextCleaner
    """
    def __init__(self):
        """
        Initialize the class
        """
        self.words_each_line = []
        self.each_line = ""

    def pre_process_text(self, line):
        """
        Clean and pre-process the text file
        String -> List
        """
        self.each_line = line
        self.each_line = self.each_line.lower().rstrip()
        self.each_line = self.each_line.replace(",", " COMMA")
        self.words_each_line = re.findall(r"[\w^\'\-]+", self.each_line)
        for item in range(len(self.words_each_line)):
            if self.words_each_line[item] == "mr.":
                self.words_each_line[item] = "mr"
            elif self.words_each_line[item] == "dr.":
                self.words_each_line[item] = "dr"
        return self.words_each_line
