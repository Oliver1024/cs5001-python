# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw12/
# Name: Kejian Tong

from game_controller import GameController

SPACE = {'w': 700, 'h': 700}

# Constant values
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
CELL_SIZE = 100

gc = GameController(BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE)


def setup():
    """setup the size and color of sketch"""
    size(SPACE['w'], SPACE['h'])
    colorMode(RGB, 1)


def draw():
    """Call function and begin to draw"""
    global score_file
    background(167, 167, 167)
    gc.draw_me(mouseX, mouseY)


def mousePressed():
    """Define mousePressed function"""
    gc.game_start = True
    gc.mouse = True


def mouseReleased():
    """Define mouseReleased function"""
    gc.mouse = False
