import turtle as t

# set the scaling
scale = 2.5

# robot dimensions
w = 30
l = 50

# set up the window slightly bigger than square
t.window_height = 600
t.window_width = 600

# create boundries
t.penup()
t.pensize(3)
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
t.shape("square")
t.shapesize(1.5, 2.5)
t.pensize(2)
t.goto(-235, -235)
t.setheading(90)
t.pendown()

# set the first i length and do one side
    # this is due to the pattern changing every 2 sides 
    # after the first side is drawn
i = 470
t.forward(i)
t.right(90)

while(i >= 0):
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(90)
    i -= 30

t.mainloop()