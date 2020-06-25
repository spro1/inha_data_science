import random
import turtle as t

#영역 잡기
def draw_maze():
    t.penup()
    t.goto(-300,-300) #x, y -300 -300
    t.pendown()
    t.forward(600) #x, y 300 -300
    t.left(90)
    t.forward(600)#x, y 300 300
    t.left(90)
    t.forward(600) #x, y -300 300
    t.left(90)
    t.forward(600) #x, y -300 -300
    t.left(90)
    t.penup();
    t.goto(0,0)
	
def turn_left():
    t.speed(4)
    t.left(5)
    t.forward(30)
    exit_program(t.xcor(), t.ycor())
        
def turn_right():
    t.speed(4)
    t.right(5)
    t.forward(30)
    exit_program(t.xcor(), t.ycor())
    


def exit_program(x, y):
    print("x좌표:",t.xcor())
    print("y좌표:",t.ycor())
    if x < -300 or x >300 or y <-300 or y >300:
        t.bye()
        print("영역 바깥으로 나가서 미션 수행을 실패 했습니다.")


screen = t.Screen()
t.speed(0)
draw_maze()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

t.penup()
t.pendown()

screen.listen()                     
screen.mainloop()
