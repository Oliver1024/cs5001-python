# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw10/
# Name: Kejian Tong

from game_controller import GameController

SPACE = {'w': 600, 'h': 600}
fadeout = 150.0

game_controller = GameController(SPACE, fadeout)


def setup():
    """setup the size and color of sketch"""
    size(SPACE['w'], SPACE['h'])
    colorMode(RGB, 1)


def draw():
    """Call function and begin to draw"""
    background(0)
    game_controller.update()


def keyPressed():
    """Defin keypress function"""
    if (key == CODED):
        game_controller.handle_keypress(key, keyCode)
    else:
        game_controller.handle_keypress(key)


def keyReleased():
    """Define key released function"""
    game_controller.handle_keyup()
