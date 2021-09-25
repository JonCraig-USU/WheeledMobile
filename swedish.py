import turtle as t

'''everything on this one was done in centimeters'''

# robot dimensions
w = 30
l = 50

# set up the window slightly bigger than square
t.window_height = 600
t.window_width = 600

# create boundries
t.penup()
t.pensize(3)
t.speed(0)
t.goto(-250, -250)
t.setheading(90)
t.pendown()
t.forward(500)
t.right(90)
t.forward(500)
t.right(90)
t.forward(500)
t.right(90)
t.forward(500)


# get to start position and siz to robot
t.penup()
t.speed(5)
t.shape("square")
t.shapesize(1.5, 2.5)
t.pensize(2)
t.goto(-235, -225 + 450)
t.setheading(90)
t.pendown()

# the first side is done seperately as it does not follow 
xMv = 470
yMv = 450
x = -235
y = -225
direc = -1
t.goto(x, y)

while(xMv >= 0 and yMv >= 0):
    direc *= -1
    x = x + direc * xMv
    t.goto(x, y)
    y = y + direc * yMv
    t.goto(x, y)
    xMv -= 15
    yMv -= 25

t.mainloop()