import turtle as t
import math

# Constant numbers
STAR_LONG = 500
HALF_NUMBER = 2
ANGLE_NUMBER = 5
CIRCLE_ANGLE = 360
STAR_RANGE = 5
# CIRCLE_ANGLE/HALF_NUMBER-(CIRCLE_ANGLE/HALF_NUMBER/STAR_RANGE)=144
STAR_RIGHT = 144

# Calculate the radius of circle
SUB_CIRCLE_ANGLE = CIRCLE_ANGLE / ANGLE_NUMBER  # 72
HALF_STAR_LONG = STAR_LONG / HALF_NUMBER  # 250
VALUE_CIRCLE = math.sin(math.radians(SUB_CIRCLE_ANGLE))  # 0.95
RADIUS = STAR_LONG / HALF_NUMBER / VALUE_CIRCLE  # RADIUS = 263


def circle(x):
    """
    Draw a circle using the radius
    Number -> None
    """
    t.pencolor('blue')
    t.penup()
    t.fillcolor('cyan')
    t.setposition(0, -(RADIUS))
    t.pendown()
    t.begin_fill()
    t.circle(x)
    t.end_fill()


def star(x, y):
    """
    Draw a star using values of x and y
    Number Number -> None
    """
    t.pencolor('red')
    t.right(SUB_CIRCLE_ANGLE)
    t.penup()
    t.fillcolor('yellow')
    t.setposition(0, RADIUS)
    t.pendown()
    t.begin_fill()

    # Using for loop to draw the star
    for i in range(STAR_RANGE):
        t.forward(x)
        t.right(y)
    t.end_fill()
    t.hideturtle()
    t.exitonclick()


def main():
    """
    Call other functions
    None -> None
    """
    circle(RADIUS)
    star(STAR_LONG, STAR_RIGHT)


main()
