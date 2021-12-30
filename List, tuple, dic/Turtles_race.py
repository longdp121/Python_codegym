import turtle
from random import choice
turtle.Screen().setup(1.0, 1.0)
#Set up race
fn = turtle.Turtle()
finish_line = 500
fn.penup()
fn.goto(finish_line, 768/2)
fn.pendown()
fn.right(90)
fn.pensize(10)
fn.fd(768)
racer_color = ["blue", "red", "green", "yellow", "black", "pink", "brown"]
x_start = -500
y_start = [0, 40, 80, 120, -40, -80, -120]
speed = [5, 10, 15, 20, 25, 30]
all_turtle = []

#Set up racers
for index in range(len(racer_color)):
    p = turtle.Turtle()
    p.shape("turtle")
    p.speed(10)
    p.color(racer_color[index])
    p.penup()
    p.goto(x_start, y_start[index])
    all_turtle.append(p)

#Race
run = True
while run:
    for i in range(0, len(racer_color)):
        (all_turtle[i]).fd(choice(speed))
        if all_turtle[i].xcor() > finish_line:
            winner = i
            run = False

result = turtle.Turtle()
result.penup()
result.goto(0, 340)
result.write(f"Congrate: {racer_color[winner]} is winner", align="center", font = ("Arial", 20, "normal"))
result.goto(-400, -400)

turtle.done()