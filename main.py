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

penup()
goto(-100,-100)
pendown()
circle(30)
done()