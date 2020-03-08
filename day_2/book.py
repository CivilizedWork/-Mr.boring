import turtle
import math
bod = turtle.Turtle()

def polugon(t,n,length):
    angle=360/n
    for i in range(n):
        bod.fd(length)
        bod.lt(angle)
def circle(t,r):
    cir=2*math.pi*r
    n = 50
    length=cir/n
    polugon(t,n,length)
circle(bod,100)
turtle.mainloop()