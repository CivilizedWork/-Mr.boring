import turtle
bod=turtle.Turtle()
def draw(t,length,n):
    if n==0:
        return
    t.fd(length * n)
    t.lt()
    draw(t, length, n - 1)
    t.rt()
    draw(t, length, n - 1)
    t.lt()
    t.bk(length * n)

draw(bod,10,5)