# Case-study #1
# Developers:   Kapinos A. (___),
#               Kovshov G. (___),
#               Pankova J. (___)
from turtle import *
import math


def square(side, position_x, position_y, rotation=0):
    '''
    Function, drawing square.
    :param position_x: coordinate x in the middle of the square
    :param position_y: coordinate y in the middle of the square
    :param side: side length of a square
    :param rotation: additional rotation angle
    :return: None
    '''
    sq = Turtle()
    sq.speed(0)
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
    sq.forward(side)
    sq.right(90)
    sq.forward(side)
    sq.right(90)
    sq.forward(side)
    sq.right(90)
    sq.forward(side)
    sq.penup()


def triangle(position_x1, position_y1, position_x2, position_y2, position_x3, position_y3):
    '''
    Function, drawing triangle.
    :param position_x1: coordinate x1 shows position of the first point horizontally
    :param position_y1: coordinate y1 shows position of the first point vertically
    :param position_x2: coordinate x2 shows position of the second point horizontally
    :param position_y2: coordinate y2 shows position of the second point vertically
    :param position_x3: coordinate x3 shows position of the third point horizontally
    :param position_y3: coordinate y3 shows position of the third point vertically
    :param side: side length of a square
    :return: None
    '''
    tr = Turtle()
    tr.speed(1)
    # setting the pen position
    tr.penup()
    tr.goto(position_x1, position_y1)
    # actually drawing the triangle
    tr.pendown()
    tr.goto(position_x2, position_y2)
    tr.goto(position_x3, position_y3)
    tr.goto(position_x1, position_y1)
    tr.penup()


def triangle_perf(side, position_x, position_y, rotation_angle=0):
    tri = Turtle()
    tri.speed(1)
    # setting the pen position
    tri.penup()
    tri.setheading(90)
    tri.goto(position_x, position_y)
    tri.right(rotation_angle)
    tri.fd(math.sqrt(3) / 3 * side)
    tri.pendown()
    # actually drawing the triangle
    tri.right(150)
    tri.forward(side)
    tri.right(120)
    tri.forward(side)
    tri.right(120)
    tri.forward(side)


square(60, -30, -30 + 80, rotation=45)
triangle(-20, 50, -40, 30, 70, -15)
triangle_perf(20, 200, 200, rotation_angle=90)

done()




def triangle():
    # TODO: (Anna)
    pass

def square():
    # TODO: (Julia)
    pass

def rombus():
    # TODO: (Greg)
    pass




penup() 
goto(-50, -50)
pendown()
begin_fill()
circle(20)
end_fill()




done()
