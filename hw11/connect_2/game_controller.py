from disk import Disk
from board import Board


class GameController:
    """A class control how to play the game"""
    def __init__(self, w, h, cell_size):
        """Initialize the class"""
        self.cell_size = cell_size
        self.board = Board(self.cell_size)
        self.w = w
        self.h = h
        self.grid = [[None for _ in range(w)] for _ in range(h)]
        self.disk = None
        self.player = "red"
        self.HALF_SIZE = 50
        self.DBLE_SIZE = 200
        self.y = 0
        self.y_vel = 10
        self.target = 0
        self.column = 0
        self.holding_disk = False
        self.game_start = False
        self.dropping = False
        self.mouse = False

    def draw_me(self, mouseX, mouseY):
        """
        Call draw_board and draw_disks functions
        Number, Number -> None
        """
        if self.check_game_over():
            self.game_over()
        if self.game_start and self.area_detected():
            self.draw_disks(mouseX, mouseY)
        for row in range(self.w):
            for column in range(self.h):
                if self.grid[row][column]:
                    self.grid[row][column].draw_disk()
        self.board.draw_board()

    def draw_disks(self, mouseX, mouseY):
        """
        Draw the effective disks
        Number, Number -> None
        """
        if self.mouse and not self.dropping:
            self.column = mouseX // self.cell_size
            if self.column >= len(self.grid[0]):
                self.column = len(self.grid[0])
            self.y = self.HALF_SIZE
        else:
            self.target = (self.get_available_row(
                self.column) + 1)*self.cell_size + self.HALF_SIZE
            if self.y < self.target:
                self.dropping = True
                self.y += self.y_vel

        if not self.check_column_full(self.column):
            disk = Disk(self.column, self.player, self.cell_size, self.y)
            disk.draw_disk()
            if self.y == self.target and self.y > self.HALF_SIZE:
                self.grid[self.get_available_row(
                    self.column)][self.column] = disk
                self.next_player()
                self.game_start = False
                self.dropping = False

    def get_available_row(self, column):
        """
        Get the actual row of the board
        Number -> Number
        """
        for row in range(self.h-1, -1, -1):
            if self.grid[row][column] is None:
                return row
        return -1

    def next_player(self):
        """
        Alternate the color of dice
        """
        if self.player == "red":
            self.player = "yellow"
        else:
            self.player = "red"

    def area_detected(self):
        """
        Check the specific area on board
        None -> Boolean
        """
        if mouseY >= 0 and mouseY <= self.cell_size and mouseX >= 0 \
                and mouseX <= self.DBLE_SIZE:
            return True
        else:
            return False

    def check_column_full(self, column):
        """
        Check if the column is full
        Number -> Boolean
        """
        if self.grid[0][column] is None:
            return False
        return True

    def game_over(self):
        """
        Get the result when game is over
        """
        TEXT_COLOR = 0
        TEXT_SIZE = 30
        TEXT_X = 10
        TEXT_Y = 50
        fill(TEXT_COLOR)
        textSize(TEXT_SIZE)
        text("GAME OVER", TEXT_X, TEXT_Y)

    def check_game_over(self):
        """
        Check if the game is over
        None -> Boolean
        """
        for col in self.grid:
            for row in col:
                if row is None:
                    return False
        return True
