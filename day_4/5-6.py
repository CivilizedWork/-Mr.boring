import turtle
def koch(t, n):

    if n<3:
        t.fd(n)
        return
    m = n/3.0
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)
def snowflake(t, n):

    for i in range(3):
        koch(t, n)
        t.rt(120)
bod=turtle.Turtle()
#koch(bod,100)
snowflake(bod,100)
turtle.mainloop()
