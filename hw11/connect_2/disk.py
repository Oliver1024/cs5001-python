class Disk:
    """A disk class"""
    def __init__(self, column, color, cell_size, y):
        """Initialize the class"""
        self.cell_size = cell_size
        self.column = column
        self.HALF_SIZE = 50
        self.PERCENT = 0.9
        self.x = column*self.cell_size + self.HALF_SIZE
        self.y = y
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.color_name = color
        if self.color_name == "red":
            # set the color as RED
            self.color = self.RED
        else:
            # set the color as yellow
            self.color = self.YELLOW

    def draw_disk(self):
        """Define how to draw a disk"""
        fill(*self.color)
        noStroke()
        circle(self.x, self.y, self.cell_size * self.PERCENT)
