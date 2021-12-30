import turtle
p = turtle.Turtle()
p.speed(10)

#Function for rectangular
def draw_rectanggular(h, w):
    for i in range(2):
        p.fd(w)
        p.left(90)
        p.fd(h)
        p.left(90)

#Function for square
def draw_square(h):
    for i in range(4):
        p.fd(h)
        p.right(90)

#Function for windows
def draw_window():
    p.backward(w * 3/4)
    p.left(90)
    p.penup()
    p.fd(h/4)
    p.pendown()
    p.right(90)
    p.fillcolor("#51F300")
    p.begin_fill()
    draw_rectanggular(h/2, w/2)
    p.end_fill()

#Function for door
def draw_door():
    p.fd(h/4)
    p.left(90)
    p.fd(h/2)
    p.right(90)
    p.fillcolor("#004DF3")
    p.begin_fill()
    draw_square(h/2)
    p.end_fill()

#Start drawing
p.penup()
p.goto(-200,-200)
p.pendown()
h = 200 #height of shape
w = 100 #wide of shape

p.fillcolor("#B74B4B")
p.begin_fill()
for i in range(2):  #Draw main house
    draw_rectanggular(h, w)
    p.fd(w)
p.end_fill()
p.backward(2*w)
p.left(90)
p.fd(h)
p.right(90)
p.fillcolor("#B74B4B")
p.begin_fill()
for i in range(2):
    draw_rectanggular(h, w)
    p.fd(w)
p.end_fill()  #End maim house
p.fillcolor("#D290D8")
p.begin_fill()
draw_square(h)  #Draw/end sub-house
p.end_fill()
draw_window()
p.penup()
p.right(90)
p.fd(h/4)
p.left(90)
p.backward(w/4)
draw_window()
p.penup()
p.right(90)
p.fd(h/4)
p.right(90)
p.fd(w/4)
p.left(90)
p.fd(h)
p.left(90)
p.fd(2 * w)
draw_window()
p.penup()
p.right(90)
p.fd(h/4)
p.left(90)
p.backward(w/4)
draw_window()
p.penup()
p.right(90)
p.fd(h/4)
p.left(90)
p.fd((w * 3/4) + w)
p.pendown()
draw_door()
turtle.done()