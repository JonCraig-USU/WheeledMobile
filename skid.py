import math
import turtle as t
import numpy as np

# MAGIC NUMBERS
scale = 15  # scale factor for windo use

w = .3     # width of the bot
l = .5     # length of the bot

vr = 0     # velocity of the right wheel
vl = 0     # velocity of the left wheel

step = .1   # time between calculations (seconds)

# radians per second
def phiDot(vl, vr, w):
    return (vr - vl)/w  

# x axis movement
def xDot(vl, vr, phi):
    return -((vr + vl) / 2) * np.sin(phi)        

# y axis movement
def yDot(vl, vr, phi):
     return ((vr + vl) / 2) * np.cos(phi) 

DoC = [5, 3, 8, 10]                          # array with numbers for duration of command 
left = [1, -1, .8, 2]                        # array with numbers for left wheel velocities
right = [1.5, -1.5, -2, 2]                   # array with numbers for right wheel velocities

t.shape("turtle")
t.speed(10)
t.penup

time = 0
t.setheading(math.pi / 2)
phi = math.pi / 2
x = 0
y = 0

for i in range (0, len(left)):
    vl = left[i]
    vr = right[i]
    dur = time + DoC[i]
    print("Angular Velocity: " + str(phiDot(vl, vr, w)) + " Radians/second")

    while time < dur:
        phi = phiDot(vl, vr, w) * time
        x += xDot(vl, vr, phi) * scale
        y += yDot(vl, vr, phi) * scale
        t.goto(x, y)
        time += step

t.mainloop()



