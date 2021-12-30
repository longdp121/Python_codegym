import turtle
p = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
p.speed(10)

#Function for drawing square
def draw_big_square(a):
    p.penup()
    p.fd(a/2)
    p.right(90)
    p.fd(a/2)
    p.pendown()
    p.right(90)
    for i in range(4):
        p.fd(a)
        p.right(90)
    p.fd(a/2)
    p.right(90)
    p.penup()
    p.fd(a/2)

def draw_small_square(b):
    for i in range(4):
        p.fd(b)
        p.right(90)

#Varible input
a = 500
b = a/3
ang = 3.6
color_list = ["#D290D8", "#ced98b", "#E72626", "#64EE31", "#E1EA28", "#28EACA", "#282BEA", "#e36340", "#E82096", "#FFFFFF"]

#Drawing
p.left(90)  #Big square
for i in range (3):
    for decor in color_list:
        p.color(decor)
        draw_big_square(a)
        p.right(ang)

p.pendown()  #Small square
for i in range (int(360/ang)):
    draw_small_square(b)
    p.right(ang)

p.penup()
p.goto(-500,-500)

turtle.done()