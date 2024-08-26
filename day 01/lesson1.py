from turtle import *

#step 1 draw a square
speed(30)

#we want paint a house

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of  square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



#drawing a fist window


penup()
goto(140,150)
pendown()

color("blue")
begin_fill()
left(30)
forward(30)
left(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
end_fill()
#drawing a second window
penup()
forward(95)
pendown()


color("blue")
begin_fill()
left(3)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)
end_fill()













exitonclick()