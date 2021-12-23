# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw11/
# Name: Kejian Tong

from game_controller import GameController

SPACE = {'w': 200, 'h': 300}

# Constant values
BOARD_WIDTH = 2
BOARD_HEIGHT = 2
CELL_SIZE = 100

gc = GameController(BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE)


def setup():
    """setup the size and color of sketch"""
    size(SPACE['w'], SPACE['h'])
    colorMode(RGB, 1)


def draw():
    """Call function and begin to draw"""
    background(1)
    gc.draw_me(mouseX, mouseY)


def mousePressed():
    """Define mousePressed function"""
    gc.game_start = True
    gc.mouse = True


def mouseReleased():
    """Define mouseReleased function"""
    gc.mouse = False
