import turtle
import math
from math import pi
p = turtle.Turtle()
p.pensize(5)

class draw_circle():
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    
    def draw(self):
        p.penup()
        p.goto(self.x, self.y)
        p.pendown()
        p.circle(self.r)
    
    def caculate_c(self):
        return (2 * pi * self.r)

    def caculate_s(self):
        return (pi * math.pow(self.r, 2))

app = draw_circle(200, -40, -40)
app.draw()
print(f"Chu vi hinh tron la {round(app.caculate_c(), 2)}")
print(f"Dien tich hinh tron la {round(app.caculate_s(), 2)}")

turtle.done()