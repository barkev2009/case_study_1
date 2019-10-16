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

speed(10)
pensize(2)
color('grey', 'pink')
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
goto(-50, 0)
pendown()
begin_fill()
setheading(45)
forward(50)
left(120)
forward(50)
left(120)
forward(50)
end_fill()

penup() 
goto(-50, -50)
pendown()
begin_fill()
circle(20)
end_fill()

#The creation of fish
color('black', 'pink')
penup()
goto(200, 200)
pendown()
begin_fill()
setheading(90)
forward(30)
right(120)
forward(60)
right(120)
forward(60)
right(120)
forward(30)

forward(60)
left(90)
forward(60)
left(135)
goto(200, 200)

setheading(270)
forward(60)
right(90)
forward(60)
goto(200, 200)

setheading(135)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

setheading(180)
penup()
goto(151, 200)
pendown()
forward(30)
goto(91, 230)
right(180)
forward(30)
goto(151, 200)

goto(121, 170)
right(180)
forward(30)
goto(121, 200)
left(90)
forward(30)


done()
