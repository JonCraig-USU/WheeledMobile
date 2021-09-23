from _typeshed import StrOrBytesPath
import turtle as t
import numpy as np

# MAGIC NUMBERS
scale = 1  # scale factor for windo use

w = .3     # width of the bot
l = .5     # length of the bot

vr = 0     # velocity of the right wheel
vl = 0     # velocity of the left wheel

step = .01   # time between calculats (seconds)

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
t.shapesize(3, 5, 1)

for i in (0, len(left)):
    vl = left[i]
    vr = right[i]
    dur = DoC[i]

    for time in range(0, DoC, step):
        phi = phiDot(vl, vr, w) * time
        x = xDot(vl, vr, phi)
        y = yDot(vl, vr, phi)
        t.dot()
        t.goto(x, y)

t.mainloop()



