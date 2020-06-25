import turtle as t

t.pensize(1)
t.penup()
t.goto(0,0)
t.pendown()

for i in range(3,9):
    for l in range(i):
        t.forward(20)
        t.left(360/i)
