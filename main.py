# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh


from turtle import Turtle, Screen

## Controls:
# Forward: w
# Backward: s
# Left: a
# Right: d
# Clear: c

t = Turtle()
t.speed(0)
t.pensize(3)
s = Screen()
s.title("Your Sketch App")

def f():
    t.forward(10)
def b():
    t.backward(10)
def l():
    t.setheading(t.heading() + 10)
def r():
    t.setheading(t.heading() - 10)
def c():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

s.listen()
s.onkey(key="w", fun=f)
s.onkey(key="s", fun=b)
s.onkey(key="a", fun=l)
s.onkey(key="d", fun=r)
s.onkey(key="c", fun=c)
s.exitonclick()