# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/lab10
# Name: Kejian Tong

# Assign values to variables
thrust_factor = 0
spaceship_x = 300
spaceship_y = 300
x_vel = 0
y_vel = 0
rotation = 0
size_x = 600
size_y = 600
circle_x = 300
circle_y = 300
circle_rad = 75
stro_num = 3
rotation_num = 3
fill_half_num = 0.5
tri_num1 = -16
tri_num2 = 10
tri_num3 = -30
tri_num4 = 16
ellipse_num1 = 100
ellipse_num2 = 300
ellipse_num3 = 500
circle_double = 2
fill_num1 = 0.8
fill_num2 = 0.9


def setup():
    """
    Setup the canvas size and background color
    """
    size(size_x, size_y)
    colorMode(RGB, 1)
    strokeWeight(stro_num)


def draw():
    """
    Call functions to draw spaceship and circles
    """
    global rotation
    global circle_x
    global circle_y  # Add another parameter
    background(0)
    circle_x = circle_x + 1
    circle_y = circle_y + 1

    # Draw a circle with the border
    if circle_y > size_y + circle_rad:
        circle_y = circle_y - size_y
    elif circle_y > circle_y - size_y:
        draw_circle_2(circle_x - size_x)
    draw_circle_2(circle_x)
    draw_spaceship()

    if circle_x > size_x + circle_rad:
        circle_x = circle_x - size_x
    elif circle_x > size_x - circle_rad:
        draw_circle_1(circle_x - size_x)
        draw_circle_3(circle_x - size_x)
    # Draw entire grey circles
    draw_circle_1(circle_x)
    draw_circle_3(circle_x)


def keyPressed():
    """
    Setup spaceship direction
    """
    global rotation
    global thrust_factor
    if (key == CODED):
        if keyCode == UP:
            thrust_factor = 0.5
        if keyCode == RIGHT:
            rotation += rotation_num
        if keyCode == LEFT:
            rotation -= rotation_num


def draw_spaceship():
    """
    Draw spaceship according velocity and x,y position
    """
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global thrust_factor
    x_vel = (x_vel + sin(radians(rotation))) * thrust_factor
    y_vel = (y_vel - cos(radians(rotation))) * thrust_factor

    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel
    pushMatrix()
    translate(spaceship_x, spaceship_y)
    rotate(radians(rotation))
    fill(0)
    stroke(1)
    strokeWeight(stro_num)
    triangle(tri_num1, tri_num2,  0, tri_num3, tri_num4, tri_num2)
    popMatrix()


def draw_circle_1(x):
    """
    Draw the first circle
    """
    fill(fill_half_num, fill_half_num, fill_half_num)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, ellipse_num1, circle_rad *
            circle_double, circle_rad*circle_double)


def draw_circle_2(x):
    """
    Draw the second circle
    """
    fill(fill_num1, fill_num2, 1.0)
    stroke(1.0, 1.0, 1.0)
    ellipse(ellipse_num2, x, circle_rad *
            circle_double, circle_rad*circle_double)


def draw_circle_3(x):
    """
    Draw the third circle
    """
    fill(fill_half_num, fill_half_num, fill_half_num)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, ellipse_num3, circle_rad *
            circle_double, circle_rad*circle_double)
