import turtle as t
import random

def make_circle(x, y, r, pen_color, fill_color):
    print("x좌표:%s, y좌표:%s, r크기:%s, 테두리 색:%s, 내부 색:%s"%(x,y,r,pen_color,fill_color)) 
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(pen_color, fill_color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

for i in range(0,10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    r = random.randint(5,20)
    pen_color = random.choice(colors)
    fill_color = random.choice(colors)
    make_circle(x, y, r, pen_color, fill_color)
