# Importing tkinter module
from tkinter import * 
from tkinter.ttk import *

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b2 = Button(master, text = "GFG")
b2.pack(fill = X, expand = True ,ipady = 20)

# button widget
b1 = Button(master, text = "Click me !")

# This is where b1 is placed inside b2 with in_ option
b1.place(in_= b2, relx = 0.5, rely = 0.5, anchor = CENTER)

# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()



















'''
class build_theme():
    def __init__(self):
        self.mainw = mainw
        self.mainh = mainh
        self.col = col
        self.row = row
    
    def test(self):
        print(self.mainw)

    def w_edge(self):
        w_unit = []
        for i in range(self.col):
            i = self.mainw / self.col
            w_unit.append(i)
        return w_unit

    def h_edge(self):
        h_unit = []
        for i in range(self.row):
            i = self.mainh /self.row
            h_unit.append(i)
        print(h_unit)

a = build_theme()
#a.test()
#a.w_edge()
a.h_edge()
'''


#w = mainloop()