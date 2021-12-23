from disk import Disk
from board import Board
import random
import time


class GameController:
    """A class control how to play the game"""

    def __init__(self, w, h, cell_size):
        """Initialize the class"""
        self.cell_size = cell_size
        self.board = Board(self.cell_size)
        self.w = w
        self.h = h
        self.grid = [[None for _ in range(w)] for _ in range(h)]
        self.player = "RED"
        self.HALF_SIZE = 50
        self.y = 0
        self.y_vel = 20
        self.target = 0
        self.column = 0
        self.game_start = False
        self.dropping = False
        self.mouse = False
        self.grid_full = False
        self.y_ai = 0
        self.row_ai = 0
        self.target_ai = 0
        self.column_ai = -1
        self.winner = None
        self.score_file = {}
        self.RANDOM_NUM = 6
        self.NUM_TWO = 2
        self.NUM_THREE = 3

    def draw_me(self, mouseX, mouseY):
        """
        Call draw_board and draw_disks functions
        Number, Number -> None
        """
        for column in range(self.w):
            for row in range(self.h):
                if self.grid[row][column]:
                    self.grid[row][column].draw_disk()
        self.board.draw_board()

        if self.is_game_over() or self.grid_full is True:
            self.game_over()
            if self.winner == "RED":
                self.read_the_score()
                self.write_the_score()
                noLoop()
        else:
            if self.player == "RED":
                if self.game_start and (self.area_detected()):
                    self.draw_disks(mouseX, mouseY)
            elif self.player == "YELLOW":
                self.ai_disk_drop()
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
        if self.player == "RED":
            self.player = "YELLOW"
        else:
            self.player = "RED"

    def area_detected(self):
        """
        Check the specific area on board
        None -> Boolean
        """
        if mouseY >= 0 and mouseY <= self.cell_size and mouseX >= 0 \
                and mouseX <= self.cell_size*self.w:
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
        TEXT_SIZE = 50
        TEXT_X = 200
        TEXT_Y = 265
        strokeWeight(50)
        fill(TEXT_COLOR)
        textSize(TEXT_SIZE)
        if self.grid_full:
            text("TIRED GAME", TEXT_X, TEXT_Y)
        elif self.winner == "RED":
            text("RED WINS", TEXT_X, TEXT_Y)
        elif self.winner == "YELLOW":
            text("YELLOW WINS", TEXT_X, TEXT_Y)

    def check_grid_full(self):
        """
        Check if the game is over
        None -> Boolean
        """
        for col in self.grid:
            for row in col:
                if row is None:
                    return False
        self.grid_full = True
        return True

    def grid_to_colors(self):
        """Get the color of disk"""
        new_grid = [[None for _ in range(self.w)] for _ in range(self.h)]
        for r in range(self.h):
            for c in range(self.w):
                if self.grid[r][c]:
                    new_grid[r][c] = self.grid[r][c].color_name
        return new_grid

    def check_winner(self):
        """
        Check if the red or yellow disk get the winner first
        None -> Boolean
        """
        color_grid = self.grid_to_colors()
        # Check horizontal locations for win
        for r in range(self.h):
            for c in range(self.w - self.NUM_THREE):
                temp_color = color_grid[r][c]
                if (color_grid[r][c] is not None
                    and color_grid[r][c+1] == temp_color
                    and color_grid[r][c+self.NUM_TWO] == temp_color
                        and color_grid[r][c+self.NUM_THREE] == temp_color):
                    self.winner = temp_color
                    return True

        # Check vertical locations for win
        for r in range(self.h-3):
            for c in range(self.w):
                temp_color = color_grid[r][c]
                if (color_grid[r][c] is not None
                    and color_grid[r+1][c] == temp_color
                    and color_grid[r+self.NUM_TWO][c] == temp_color
                        and color_grid[r+self.NUM_THREE][c] == temp_color):
                    self.winner = temp_color
                    return True

        # Check positively sloped diaganols
        for r in range(self.h-self.NUM_THREE):
            for c in range(self.w-self.NUM_THREE):
                temp_color = color_grid[r][c]
                if (color_grid[r][c] is not None
                    and color_grid[r+1][c+1] == temp_color
                    and color_grid[r+self.NUM_TWO][c+self.NUM_TWO]
                    == temp_color
                        and color_grid[r+self.NUM_THREE][c+self.NUM_THREE]
                        == temp_color):
                    self.winner = temp_color
                    return True

        # Check negatively sloped diaganols
        for r in range(self.NUM_THREE, self.h):
            for c in range(self.w-self.NUM_THREE):
                temp_color = color_grid[r][c]
                if (color_grid[r][c] is not None
                    and color_grid[r-1][c+1] == temp_color
                    and color_grid[r-self.NUM_TWO][c+self.NUM_TWO]
                    == temp_color
                        and color_grid[r-self.NUM_THREE][c+self.NUM_THREE]
                        == temp_color):
                    self.winner = temp_color
                    return True

    def ai_disk_drop(self):
        """Make ai pick a legal random disk move and drop disk"""
        if self.column_ai == -1:
            time.sleep(1)
            self.column_ai = random.randint(0, self.RANDOM_NUM)
            self.y_ai = self.HALF_SIZE
        else:
            self.row_ai = self.get_available_row(self.column_ai)
            self.target_ai = (self.row_ai + 1)*self.cell_size + self.HALF_SIZE
            if self.y_ai < self.target_ai:
                self.y_ai += self.y_vel

        if not self.check_column_full(self.column_ai):
            disk_ai = Disk(self.column_ai, self.player,
                           self.cell_size, self.y_ai)
            disk_ai.draw_disk()

            if self.y_ai >= self.target_ai and self.y_ai > self.HALF_SIZE:
                self.grid[self.row_ai][self.column_ai] = disk_ai
                self.next_player()
                self.column_ai = -1
                self.y_ai = self.HALF_SIZE
        else:
            self.column_ai = -1

    def is_game_over(self):
        """
        Check if game is over or not
        None -> Boolean
        """
        if self.check_winner() is True:
            self.game_start = False
            return True
        else:
            return False

    def input(self, message=''):
        """Prompp name to users"""
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def read_the_score(self):
        '''
        Read the name and score, then sort them.
        None -> None
        '''
        f = open("scores.txt", 'r')
        for line in f:
            score_list = line.rstrip().split()
            score = score_list[-1]
            score_list.pop(-1)
            name = ' '.join(score_list)
            self.score_file[name] = int(score)
        f.close()

    def write_the_score(self):
        '''
        Write the name and corresponding score.
        None -> None
        '''
        name = self.input('Please enter your name')
        while(name is None or name == ''):
            name = self.input('Please enter your name')
        if name in self.score_file.keys():
            self.score_file[name] += 1
        else:
            self.score_file[name] = 1
        player_names = self.top_n_counts()

        f = open("scores.txt", "w")
        for score in player_names:
            s = score[0] + ' ' + str(score[1]) + '\n'
            f.write(s)
        f.close()

    def top_n_counts(self):
        '''
        Sort the scores in a descending
        order.
        None -> List
        '''
        return sorted(
            self.score_file.items(),
            key=lambda x: x[1],
            reverse=True)
