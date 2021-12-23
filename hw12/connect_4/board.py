class Board:
    """A board class"""

    def __init__(self, cell_size):
        """Initialize the class"""
        self.size = cell_size
        self.RANGE = 8
        self.color_board = (0, 0, 255)
        self.weight_value = 20

    def draw_board(self):
        """Begin to draw the board"""
        strokeWeight(self.weight_value)
        stroke(*self.color_board)

        for i in range(1, self.RANGE):
            line(0, i*self.size, self.size*self.RANGE, i*self.size)

        for j in range(0, self.RANGE):
            line(j*self.size, self.size,
                 self.size*j, self.size*self.RANGE)
