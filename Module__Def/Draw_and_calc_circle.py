import turtle
import math as m
from math import pi
p = turtle.Turtle()
p.speed(10)

#Function for drawing circle
def draw_circle(a):
    '''
    Draw a circle
    a = input = r
    '''
    p.circle(a)

#Function for cacultate circle
def calc_circle(a):
    '''
    Caculate circle area
    a = input = r
    '''
    print(pi*m.pow(a,2))

a = int(input("Enter radius: "))
draw_circle(a)
calc_circle(a)
turtle.done()