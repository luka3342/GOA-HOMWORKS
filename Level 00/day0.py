from turtle import*
color("green")
width(5)    
speed(10)   # drawing a squer
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


left(90)   # drawing a door
forward(75)
color("yellow")
begin_fill()
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
end_fill()

penup()    # drawing a roof
goto(200,200)
pendown()
color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()   # drawing a windows
goto(20,185)
pendown()
left(30)
color("purple")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)



penup()  
goto(180,185)
pendown()

color("purple")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

exitonclick()