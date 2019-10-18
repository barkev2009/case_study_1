# Case-study #1
# Developers:   Kapinos A. (___),
#               Kovshov G. (___),
#               Pankova J. (___)
from turtle import *
import math


def square(side, position_x, position_y, fig_color='black', rotation=0):
    '''
    Function, drawing square.
    :param position_x: coordinate x in the middle of the square
    :param position_y: coordinate y in the middle of the square
    :param side: side length of a square
    :param fig_color: fills the figure with the selected color
    :param rotation: the rotation angle that determines the position of the figure
    :return: None
    '''
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

    # actually drawing the triangle
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
    '''
    Function, drawing triangle.
    :param position_x1: coordinate x1 shows position of the first point horizontally
    :param position_y1: coordinate y1 shows position of the first point vertically
    :param position_x2: coordinate x2 shows position of the second point horizontally
    :param position_y2: coordinate y2 shows position of the second point vertically
    :param position_x3: coordinate x3 shows position of the third point horizontally
    :param position_y3: coordinate y3 shows position of the third point vertically
    :param fig_color: fills the figure with the selected color
    :return: None
    '''
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


def triangle_perf(side, position_x, position_y, fig_color='black', rotation_angle=0):
    '''
    Function, drawing triangle.
    :param side: side length of a perfect triangle
    :param position_x: coordinate x in the middle of the perfect triangle
    :param position_y: coordinate y in the middle of the perfect triangle
    :param fig_color: fills the figure with the selected color
    :param rotation_angle: the rotation angle that determines the position of the figure
    :return: None
    '''
    tri = Turtle()
    tri.speed(0)
    tri.hideturtle()
    tri.color(fig_color)

    # setting the pen position
    tri.penup()
    tri.setheading(90)
    tri.goto(position_x, position_y)
    tri.right(rotation_angle)
    tri.fd(math.sqrt(3) / 3 * side)
    tri.pendown()

    # actually drawing the triangle
    tri.begin_fill()
    tri.right(150)
    tri.forward(side)
    tri.right(120)
    tri.forward(side)
    tri.right(120)
    tri.forward(side)
    tri.end_fill()
    tri.penup()


def parallelogram(position_x, position_y, side_horiz, side_angled, paral_angle, fig_color='black', rotation_angle=0):
    '''
    Function, drawing triangle.
    :param position_x: upper left coordinate x
    :param position_y: upper left coordinate y
    :param side_horiz: lenght of the horizontal line of the parallelogram
    :param side_angled: lenght of the line at an angle
    :param fig_color: fills the figure with the selected color
    :param rotation_angle: the rotation angle that determines the position of the figure
    :return: None
    '''
    par = Turtle()
    par.speed(1)
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


'''Creation of the fish'''
square(42, 200, 200, rotation=45, fig_color='orange red')
triangle(295, 200, 235, 230, 235, 170, 'deep sky blue')
triangle(230, 210, 230, 270, 170, 270, 'red')
triangle(230, 190, 230, 130, 170, 130, 'yellow')
triangle(165, 200, 135, 200, 135, 170, 'violet')
triangle(130, 170, 130, 200, 100, 170, 'dark violet')
parallelogram(100, 235, 44, 35, 45, rotation_angle=-45, fig_color='lawn green')

done()
