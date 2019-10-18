# Case-study #1
# Developers:   Kapinos A. (35%),
#               Kovshov G. (40%),
#               Pankova J. (25%)
from turtle import *
import math


def square(side, position_x, position_y, fig_color='black', rotation=0):
    """
    Function, drawing square.
    :param position_x: coordinate x in the middle of the square
    :param position_y: coordinate y in the middle of the square
    :param fig_color: color of the figure
    :param side: side length of a square
    :param rotation: additional rotation angle
    :return: None
    """
    sq = Turtle()
    sq.speed(0)
    sq.hideturtle()
    sq.color(fig_color)

    # setting the pen position
    sq.penup()
    sq.goto(position_x, position_y)
    sq.right(90 + rotation)
    sq.forward(side / 2)
    sq.right(90)
    sq.forward(side / 2)
    sq.right(90)

    # actually drawing the square
    sq.pendown()
    sq.begin_fill()
    sq.forward(side)
    sq.right(90)
    sq.forward(side)
    sq.right(90)
    sq.forward(side)
    sq.right(90)
    sq.forward(side)
    sq.end_fill()
    sq.penup()


def triangle(position_x1, position_y1, position_x2, position_y2, position_x3, position_y3, fig_color='black'):
    """
    Function, drawing triangle.
    :param position_x1: coordinate x1 shows position of the first point horizontally
    :param position_y1: coordinate y1 shows position of the first point vertically
    :param position_x2: coordinate x2 shows position of the second point horizontally
    :param position_y2: coordinate y2 shows position of the second point vertically
    :param position_x3: coordinate x3 shows position of the third point horizontally
    :param position_y3: coordinate y3 shows position of the third point vertically
    :param fig_color: color of the figure
    :return: None
    """
    tr = Turtle()
    tr.speed(10)
    tr.hideturtle()
    tr.color(fig_color)

    # setting the pen position
    tr.penup()
    tr.goto(position_x1, position_y1)

    # actually drawing the triangle
    tr.pendown()
    tr.begin_fill()
    tr.goto(position_x2, position_y2)
    tr.goto(position_x3, position_y3)
    tr.goto(position_x1, position_y1)
    tr.end_fill()
    tr.penup()


def triangle_right_isosceles(side, position_x, position_y, fig_color='black', rotation_angle=0):
    """
    The function of drawing the right triangle, which is also isosceles (has two identical sides).
    :param side: the isosceles side of the right-angled triangle
    :param position_x: x-coordinate of the right angle
    :param position_y: y-coordinate of the right angle
    :param fig_color: the color of the figure
    :param rotation_angle: the rotation angle of the triangle (rotates around the right angle)
    :return: None
    """
    tri = Turtle()
    tri.speed(0)
    tri.hideturtle()
    tri.color(fig_color)

    # setting the pen position
    tri.penup()
    tri.setheading(-135)
    tri.goto(position_x, position_y)
    tri.right(rotation_angle)
    tri.pendown()

    # actually drawing the triangle
    tri.begin_fill()
    tri.forward(side)
    tri.left(135)
    tri.forward(math.sqrt(side**2 + side**2))
    tri.left(135)
    tri.forward(side)
    tri.end_fill()
    tri.penup()


def parallelogram(x, y, side_horiz, side_angled, paral_angle, fig_color='black', rotation_angle=0):
    """
    The function of drawing the parallelogram with given sides, angle, its position and whether it should be rotated.
    :param x: x-coordinate of the low-left angle
    :param y: y-coordinate of the low-left angle
    :param side_horiz: the horizontal side of the figure
    :param side_angled: the adjacent side
    :param paral_angle: the degree of the low-left angle between two sides
    :param fig_color: the figure's color
    :param rotation_angle: the angle of figure's rotation (rotates around the low-left angle)
    :return: None
    """
    par = Turtle()
    par.speed(0)
    par.hideturtle()
    par.color(fig_color)

    # setting the turtle's position
    par.penup()
    par.goto(x, y)
    par.left(paral_angle + rotation_angle)
    par.pendown()

    # actually drawing the figure
    par.begin_fill()
    par.forward(side_angled)
    par.right(paral_angle)
    par.forward(side_horiz)
    par.right(180 - paral_angle)
    par.forward(side_angled)
    par.right(paral_angle)
    par.forward(side_horiz)
    par.end_fill()
    par.penup()


'''Creation of fish'''
square(42, 200, 150, rotation=45, fig_color='orange red')
triangle_right_isosceles(88, 233, 241, 'red', 45)
triangle_right_isosceles(40, 126, 148, 'violet', -45)
triangle_right_isosceles(61, 281, 150, 'deep sky blue', 90)
triangle_right_isosceles(40, 121, 107, 'dark violet', 135)
triangle_right_isosceles(88, 233, 59, 'yellow', 135)
parallelogram(167, 152, 61, 44, 45, 'lawn green', 135)

'''Creation of the rocket'''
square(28, -220, -240, rotation=45, fig_color='orange red')
triangle(-200, -100, -180, -120, -220, -120, fig_color='violet')
triangle(-220, -125, -180, -125, -180, -165, 'deep sky blue')
triangle(-220, -130, -220, -210, -180, -170, 'yellow')
triangle(-220, -215, -180, -175, -180, -255, 'red')
triangle(-242, -242, -240, -282, -222, -262, fig_color='dark violet')
triangle(-178, -258, -140, -258, -178, -215, 'lawn green')
triangle(-140, -282, -178, -260, -140, -260, 'lawn green')

'''Creation of the boat'''
square(42, -101, 99, rotation=45, fig_color='orange red')
triangle_right_isosceles(88, -103, 132, 'red', 90)
triangle_right_isosceles(40, -133, 96, 'violet')
triangle_right_isosceles(61, -150, 21, 'deep sky blue', 180)
triangle_right_isosceles(40, -164, 198, 'dark violet', -135)
triangle_right_isosceles(88, -169, 83, 'yellow', 135)
parallelogram(-156, 21, 61, 44, 45, 'lawn green', 135)

'''Creation of the SQUARE'''
square(42, -70, -100, rotation=45, fig_color='orange red')
triangle_right_isosceles(88, -102, -98, 'red', 180)
triangle_right_isosceles(40, -102, -102, 'violet')
triangle_right_isosceles(61, -40, -165, 'deep sky blue', 135)
triangle_right_isosceles(40, -68, -68, 'dark violet', -90)
triangle_right_isosceles(88, -105, -100, 'yellow', 90)
parallelogram(-165, -165, 61, 44, 45, 'lawn green')

'''Creation of the bee'''
square(42, 300, 0, rotation=45, fig_color='orange red')
triangle_right_isosceles(40, 347, -40, 'violet', 180)
triangle_right_isosceles(40, 377, -15, 'dark violet')
triangle_right_isosceles(80, 380, -15, 'yellow', -90)
triangle_right_isosceles(80, 496, -15, 'red', 90)
parallelogram(439, 42, 61, 44, 45,  fig_color='lawn green')
triangle_right_isosceles(50, 400, 77, 'deep sky blue')

'''Creation of the squirrel'''
square(42, 170, -100, fig_color='orange red')
triangle_right_isosceles(88, 99, -68, 'red', 45)
triangle_right_isosceles(40, 177, -47, 'violet')
triangle_right_isosceles(61, 56, -21, 'deep sky blue')
triangle_right_isosceles(40, 136, -185, 'dark violet', -90)
triangle_right_isosceles(88, 103, -125, 'yellow', -45)
parallelogram(42, -166, 61, 44, 45, 'lawn green', 90)

done()