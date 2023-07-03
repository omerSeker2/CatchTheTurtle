import turtle
import random

#Variables
screen = turtle.Screen()
score = turtle.Turtle()
countdown = turtle.Turtle()
t = turtle.Turtle()
point = 0
time = 20
game_over = False

#Screen Attr
screen.title("Catch The Turtle")
screen.bgcolor("light blue")

#Score Attr
def score_func():
    score.color("red")
    score.penup()
    score.hideturtle()

    top_height = screen.window_height()/2
    y = top_height - top_height/10
    score.setposition(0, y)
    score.write(arg='Score: {}'.format(str(point)), move=False, align='center', font=(30))

def increase_point(x,y):
    global point
    point += 1
    score.clear()
    score.write(arg='Score: {}'.format(str(point)), move=False, align='center', font=(30))

#Countdown Attr
def countdown_func(time):
    global game_over
    countdown.color("black")
    countdown.penup()
    countdown.hideturtle()

    top_height = screen.window_height() / 2
    y = top_height - top_height / 20
    countdown.setposition(0, y-35)
    countdown.clear()

    if time > 0:
        countdown.clear()
        countdown.write(arg='Time: {}'.format(str(time)), move=False, align='center', font=(30))
        screen.ontimer(lambda: countdown_func(time - 1), 1000)
    else:
        game_over = True
        countdown.clear()
        countdown.write(arg='Game Over!', move=False, align='center', font=(30))
        t_hide_func()


def t_func():
    t.color("dark green")
    t.penup()
    t.shape("turtle")
    t.shapesize(2)

def t_hide_gen_func():
    if not game_over:
        t.hideturtle()

        x_coordinate = random.randint(-250, 250)
        y_coordinate = random.randint(-200, 200)
        t.goto(x_coordinate, y_coordinate)
        t.showturtle()

        screen.ontimer(t_hide_gen_func, 750)

def t_hide_func():
    t.hideturtle()

t.onclick(increase_point)

turtle.tracer(0)

score_func()
countdown_func(time)
t_func()
t_hide_gen_func()

turtle.tracer(1)

turtle.mainloop()