from tkinter import *
#from tkinter import messagebox
w = Tk()
w.geometry("800x300")

#Window title
w.title("Convert App")

#Function
def convert():
    for index in range(0, 3):
        result_list[index] = float(enter_entry.get()) * convert_unit[index]
    gram_result.config(text = result_list[0])
    pound_result.config(text = result_list[1])
    ounce_result.config(text = result_list[2])

#Some list
result_list = [0, 0, 0]
convert_unit = [1000, 2.20462, 35.274]

#Entry kilogram
enter_txt = Label(w, text = "Enter the weight in kilogram")
enter_txt.grid(column = 1, row = 1)
enter_entry = Entry(w)
enter_entry.grid(column = 2, row = 1)

#Button
convert_bt = Button(w, text = "Convert", command = convert)
convert_bt.grid(column = 3, row = 1)

#Label and text
gram_txt = Label(w, text = "Gram")  #Gram label
gram_txt.grid(column = 1, row = 2)
gram_result = Label(w, text = "0")  #Gram result after convert
gram_result.grid(column = 1, row = 3)

pound_txt = Label(w, text = " Pounds")  #Pound label
pound_txt.grid(column = 2, row = 2)
pound_result = Label(w, text = "0")  #Pound result after convert
pound_result.grid(column = 2, row = 3)

ounce_txt = Label(w, text = "Ounce")  #Ounce label
ounce_txt.grid(column = 3, row = 2)
ounce_result = Label(w, text = "0")  #Ounce result after convert
ounce_result.grid(column = 3, row = 3)

w = mainloop()