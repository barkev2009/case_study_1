#Case 1

def triangle():
    # TODO: (Anna)
    pass

def square():
    # TODO: (Julia)
    pass

def rombus():
    # TODO: (Greg)
    pass

from turtle import *
import math

speed(1)
pensize(2)
color('grey','pink')
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

penup()
goto(-100,0)
pendown()
setheading(45)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
hideturtle()


apple = Turtle()

def polygon(t, n, length):
    for i in range(n):
        left(360/n)
        forward(length)

def draw_circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
    exitonclick()

draw_circle(apple, 30)
