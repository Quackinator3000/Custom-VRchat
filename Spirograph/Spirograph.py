## This is a simple spirograph program using the turtle module in python

import turtle
 
turtle.bgcolor("white") ## Color of window background (white and black work best)

LIMIT = 150 ## How many lines to draw before quiting
rotate = 173 ## How many degrees will the pen rotate
length = 100 ## How long a line to draw before rotating

COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "magenta"]

pen = turtle.Turtle()
pen.pensize(3) ## arbitrary pen size is arbitrary

s = turtle.getscreen()

i = 0
j = 0
while i < LIMIT:
    pen.pencolor(COLORS[j])
    pen.fd(length)
    pen.lt(rotate)
    i = i + 1
    j = j + 1
    if j >= 7:
        j = 0 ## once at the end of the color list, go back to 0
    length = length + 1 ## This alows the pen to increase its radius / increase segment length for spirals, comment out to disable
