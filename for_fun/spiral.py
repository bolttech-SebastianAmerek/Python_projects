import turtle

def draw_squares(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

wn = turtle.Screen()
wn.bgcolor("white")

t = turtle.Turtle()
t.speed(1)
t.color("blue")

for i in range(200):
    draw_squares(t, i)
    t.right(15)

turtle.done( )