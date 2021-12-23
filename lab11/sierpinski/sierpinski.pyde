# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab11
# Name: Kejian Tong

# ControlP5 is a 3rd party library that gives us
# interface controls. We need it for the slider.
add_library('controlP5')
from controlP5 import ControlP5
from controlP5 import Slider
from point import Point

# Here we import the Point class definition from
# the other tab of this sketch. That file is
# and ordinary .py file stored in the same
# sketch directory.

# For setting up the slider
MIN_DEPTH = 0
MAX_DEPTH = 8

# Coords of starting triangle
TOP_X = 200
TOP_Y = 100
LEFT_X = 50
LEFT_Y = 350
RIGHT_X = 350
RIGHT_Y = 350

startLeft = Point(LEFT_X, LEFT_Y)
startRight = Point(RIGHT_X, RIGHT_Y)
startTop = Point(TOP_X, TOP_Y)

# Controls the recursive depth
depth = 0


# This code is executed only once, at the beginning
# of your sketch. Conceptually, the setup function has
# a similar role to a class's constructor
def setup():
    """Setup the sketch"""
    size(430, 400)
    noStroke()
    setupSlider()


# The draw method is executed repeatedly, coinciding
# with screen refreshes. Anything that needs to be
# redrawn, recalculated, animated, or to respond to
# user interaction will need to be carried out within the
# draw loop.
def draw():
    """Begin to draw the triangles"""
    background(0)

    # Draws the initial white triangle
    fill(255)
    triangle(startLeft.getX(), startLeft.getY(),
             startRight.getX(), startRight.getY(),
             startTop.getX(), startTop.getY())
    sierpinksi(startLeft, startRight, startTop, depth)


# This is a recursive function that draws the Sierpinski triangle
def sierpinksi(bottomLeft, bottomRight, top, recursionDepth):
    """Recursively draw a triangle"""
    # Fill this in
    if recursionDepth == 0:
        return
    else:
        mid_left = bottomLeft.midPoint(top)
        mid_right = bottomRight.midPoint(top)
        mid_top = bottomRight.midPoint(bottomLeft)
        fill(0)
        triangle(mid_top.getX(), mid_top.getY(), mid_left.getX(),
                 mid_left.getY(), mid_right.getX(), mid_right.getY())
        if recursionDepth >= 1 and recursionDepth <= MAX_DEPTH:
            sierpinksi(mid_top, bottomRight, mid_right, recursionDepth - 1)
            sierpinksi(bottomLeft, mid_top, mid_left, recursionDepth - 1)
            sierpinksi(mid_left, mid_right, top, recursionDepth - 1)

# The code below sets up the slider and sets a listener callback
# function to respond to the user sliding the slider.


def setupSlider():
    """Define the slider"""
    cp5 = ControlP5(this)
    depthSlider = cp5.addSlider("Recursion Depth")\
        .setPosition(20, 20)\
        .setSize(200, 40)\
        .setRange(MIN_DEPTH, MAX_DEPTH)\
        .setNumberOfTickMarks(9)\
        .addListener(listener)


def listener(event):
    """A listener of slider to monitor the value"""
    global depth
    depth = event.value()
