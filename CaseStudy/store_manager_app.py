import csv
import datetime as dt
from random import randint
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

################ Main csv file ################
path = "db\database.csv"
file = open(path, "r+", newline = "", encoding = "utf-8-sig")
reader = csv.reader(file)

header = next(reader)
data = []
for line in reader:
    code = str(line[0])  #Product code
    name = str(line[1])  #Product name
    price = float(line[2])  #Product price
    inventory = int(line[3])  #Inventory num
    data.append([code, name, price, inventory])

#
#Class main_database
class main_database():
    def __init__(self):
        self.data = data

    def search(self, search_product):
        '''
        This func check if entry exsit in code list
        Return index or false
        '''
        for index in range(0, len(self.data)):
            if search_product == self.data[index][0]:
                return index
            else:
                continue
        return "False"

    def edit_name(self, index, new_name):
        '''
        This func edit name
        '''
        if new_name != "":
            self.data[index][1] = new_name
        else:
            pass

    def edit_price(self, index, new_price):
        '''
        This func edit price
        '''
        if new_price != "":
            self.data[index][2] = float(new_price)
        else:
            pass

    def edit_inventory(self, index, new_inventory):
        '''
        This func edit inventory
        Inventory won't be replate but +=
        '''
        if new_inventory != "":
            self.data[index][3] += int(new_inventory)
        else:
            pass

    def add(self, new_code, new_name, new_price, new_inventory):
        '''
        This func add new item
        Code must be unique
        '''
        for index in range(0, len(self.data)):
            if new_code != self.data[index][0]:
                pass
            else:
                return "False"
        self.data.append([new_code, new_name, new_price, new_inventory])
    
    def delete(self, index):
        '''
        This func delete item based on index
        '''
        self.data.pop(index)


################ Invoice csv file ################
invoice_path = "db\invoice.csv"
invoice_file = open(invoice_path, "r+", newline = "", encoding = "utf-8-sig")
invoice_reader = csv.reader(invoice_file)

invoice_header = next(invoice_reader)
invoice_data = [line for line in invoice_reader]

#
#Class invoice_database
class invoice_database():
    def __init__(self):
        self.data = data
        self.invoice_data = invoice_data

    def product_name(self):
        all_name = []
        for index in range(len(self.data)):
            all_name.append(self.data[index][1])
        return all_name

    def new_code(self):
        y = str(dt.datetime.now().strftime("%y"))
        m = str(dt.datetime.now().strftime("%m"))
        d = str(dt.datetime.now().strftime("%d"))
        random_num = str(randint(100, 999))
        invoice_code = y + m + d + random_num
        return invoice_code

    def invoice_row_tool(self):

        pass
    
main = main_database()
invoice = invoice_database()
#print(main.show())
#print(main.edit())
#print(main.add())
#print(main.delete())
#print(header)
#print(data[0][0])
#print()
print(invoice_header)
#invoice.add()
#print(invoice.product_name())
print(invoice.new_code())
print(invoice_data)


################ GUI ################

class window():
    def __init__(self, x, y):
        '''
        This func creat main windows
        '''
        self.w = Tk()
        self.x = x
        self.y = y
        self.w.geometry(f"{self.x}x{self.y}")
        self.w.title("Store manager system 1.3")
        self.data = data

    def all_gui_funcs(self):
        self.tab()
        self.main_store_manager_frame()
        self.main_invoice_frame()
        self.submain_search_frame()
        self.submain_add_frame()
        self.submain_search_result()
        self.submain_header()
        self.submain_show_data()

    def tab(self):
        '''
        This func creat tab bar
        Parent is self.w
        '''
        def store_button():
            '''
            This func switch into store frame
            '''
            self.invoice_manager_frame.pack_forget()
            self.store_manager_frame.pack()
        
        def invoice_button():
            '''
            This func switch into invoice frame
            '''
            self.store_manager_frame.pack_forget()
            self.invoice_manager_frame.pack()
            
        self.tab_frame = Frame(self.w, width = self.x)
        self.tab_frame.pack()
        self.store_button_frame = Frame(self.tab_frame, width = self.x / 2)
        self.store_button_frame.pack(side = LEFT)
        self.invoice_button_frame = Frame(self.tab_frame, width = self.x / 2)
        self.invoice_button_frame.pack(side = RIGHT)
        store_manager_button = Button(self.store_button_frame, text = "Store Manage", command = store_button, width = 20).pack()
        invoice_manager_button = Button(self.invoice_button_frame, text = "Invoice", command = invoice_button, width = 20).pack()
    
    def main_store_manager_frame(self):
        '''
        This func creat main frame for store manager app
        Parent is self.w
        Store manager is pack by default
        '''
        is_clicked = False
        self.store_manager_frame = Frame(self.w, width = self.x)
        self.store_manager_frame.pack()
    
    def submain_search_frame(self):
        '''
        This func creat frame for search
        Parent is self.store_manager_frame
        '''
        def search():
            '''
            This func unpack show_data_frame and pack search_resutl_frame
            If enter code is correct, product will be display in search_result_frame
            Search button is disable if search entry empty
            '''
            search_product = search_entry.get()
            if search_product != "":
                if main.search(search_product) != "False":
                    self.show_data_frame.pack_forget()
                    self.search_result_frame.pack()
                    self.row_tool(main.search(search_product), self.search_result_frame)
                    global is_clicked
                    is_clicked = True
                    return
                else:
                    messagebox.showinfo(title = None, message = "Product code not found.")
            else:
                pass
        
        def done():
            '''
            This func bring back show_data_frame after done searching
            search_result_frame will be clear when done
            show_data_frame be clear and renew in order to display new update realtime
            Done button is disable if search entry empty
            '''
            global is_clicked
            if is_clicked == True:
                search_product = search_entry.get()
                if search_product != "":
                    self.search_result_frame.pack_forget()
                    for widgets in self.search_result_frame.winfo_children():
                        widgets.destroy()
                    for products_widgets in self.show_data_frame.winfo_children():
                        products_widgets.destroy()
                    self.submain_show_data()
                    search_entry.delete(0, END)
                    is_clicked = False
                    return
                else:
                    pass
            else:
                pass
        self.seach_frame = Frame(self.store_manager_frame, width = self.x)
        self.seach_frame.pack()
        search_label = Label(self.seach_frame, text = "Search product by code", width = 20).grid(column = 1, row = 0)
        search_entry = Entry(self.seach_frame, width = 20)
        search_entry.grid(column = 2, row = 0)
        search_button = Button(self.seach_frame, text = "Search", command = search, width = 20).grid(column = 3, row = 0)
        done_button = Button(self.seach_frame, text = "Done", command = done, width = 20).grid(column = 4, row = 0)
        #extra_label = Label(self.seach_frame, width = 20).grid(column = 5, row = 0)
    
    def submain_add_frame(self):
        '''
        This func creat frame for add new product
        Parent is self.store_manager_frame
        '''
        def add_button():
            '''
            This func add new item to database
            show_data_frame be clear and renew in order to show update in realtime
            All entry be clear when done
            '''
            new_code = str(new_code_entry.get())
            new_name = str(new_name_entry.get())
            new_price = float(new_price_entry.get())
            new_inventory = int(new_inventory_entry.get())
            if new_code != "":
                if main.add(new_code, new_name, new_price, new_inventory) != "False":
                    main.add(new_code, new_name, new_price, new_inventory)
                    for products_widgets in self.show_data_frame.winfo_children():
                        products_widgets.destroy()
                    self.show_data_frame.pack_forget()  #unpack show_data_frame before submain_show_data() called
                    self.submain_show_data()
                    for entry_widgets in [new_code_entry, new_name_entry, new_price_entry, new_inventory_entry]:
                        entry_widgets.delete(0, END)
                else:
                    messagebox.showinfo(title = None, message = "Product code alreadt exict.")
            else:
                pass

        self.add_product_frame = Frame(self.store_manager_frame, width = self.x)
        self.add_product_frame.pack()

        new_code_label = Label(self.add_product_frame, text = "New code", width = 20).grid(column = 1, row = 0)
        new_code_entry = Entry(self.add_product_frame, width = 20)
        new_code_entry.grid(column = 2, row = 0)

        new_name_label = Label(self.add_product_frame, text = "New name", width = 20).grid(column = 3, row = 0)
        new_name_entry = Entry(self.add_product_frame, width = 20)
        new_name_entry.grid(column = 4, row = 0)
        #extra_label = Label(self.add_product_frame, width = self.x - 20 * 4).grid(column = 5, row = 0)
        
        new_price_label = Label(self.add_product_frame, text = "New price", width = 20).grid(column = 1, row = 1)
        new_price_entry = Entry(self.add_product_frame, width = 20)
        new_price_entry.grid(column = 2, row = 1)
        
        new_inventory_label = Label(self.add_product_frame, text = "New inventory", width = 20).grid(column = 3, row = 1)
        new_inventory_entry = Entry(self.add_product_frame, width = 20)
        new_inventory_entry.grid(column = 4, row = 1)
        #extra_lebel = Label(self.add_product_frame, width = self.x - 4 * 20).grid(column = 5, row = 1)

        add_new_button = Button(self.add_product_frame, text = "Add new", command = add_button).grid(column = 1, row = 3)

    def row_tool(self, index, frame):
        '''
        This func creat a row tool to show, edit and delete data
        '''
        def switch():
            '''
            This func for eddit button
            '''
            show_name.pack_forget()
            show_price.pack_forget()
            show_inventory.pack_forget()
            edit_name.pack(side = LEFT)
            save_name_button.pack(side = LEFT)
            edit_price.pack(side = LEFT)
            save_price_button.pack(side = LEFT)
            edit_invnetory.pack(side = LEFT)
            save_inventory_button.pack(side = LEFT)
        
        def delete():
            '''
            This func for delete button
            show_data_frame be clear and renew in order to show update in realtime
            '''
            main.delete(index)
            for product_widgets in self.show_data_frame.winfo_children():
                product_widgets.pack_forget()
            self.show_data_frame.destroy()
            self.submain_show_data()

        def save_name():
            new_name = edit_name.get()
            main.edit_name(index, new_name)
            edit_name.delete(0, END)
            edit_name.pack_forget()
            save_name_button.pack_forget()
            show_name.pack()
            show_name.config(text = self.data[index][1])
            
        def save_price():
            new_price = edit_price.get()
            main.edit_price(index, new_price)
            edit_price.delete(0, END)
            edit_price.pack_forget()
            save_price_button.pack_forget()
            show_price.pack()
            show_price.config(text = self.data[index][2])

        def save_inventory():
            new_invetory = edit_invnetory.get()
            main.edit_inventory(index, new_invetory)
            edit_invnetory.delete(0, END)
            edit_invnetory.pack_forget()
            save_inventory_button.pack_forget()
            show_inventory.pack()
            show_inventory.config(text = self.data[index][3])

        self.index = index
        self.row = Frame(frame)
        self.row.pack()
        code_frame = Frame(self.row)
        code_frame.pack(side = LEFT)
        name_frame = Frame(self.row)
        name_frame.pack(side = LEFT)
        price_frame = Frame(self.row)
        price_frame.pack(side = LEFT)
        inventory_frame = Frame(self.row)
        inventory_frame.pack(side = LEFT)
        buttons_frame = Frame(self.row)
        buttons_frame.pack(side = LEFT)
        
        show_code = Label(code_frame, text = self.data[self.index][0], width = 20)
        show_code.pack()

        show_name = Label(name_frame, text = self.data[self.index][1], width = 20)
        edit_name = Entry(name_frame, width = 18)
        save_name_button = Button(name_frame, text = "Save", command = save_name, width = 3)
        show_name.pack()

        show_price = Label(price_frame, text = self.data[self.index][2], width = 20)
        edit_price = Entry(price_frame, width = 18)
        save_price_button = Button(price_frame, text = "Save", command = save_price, width = 3)
        show_price.pack()

        show_inventory = Label(inventory_frame, text = self.data[self.index][3], width = 20)
        edit_invnetory = Entry(inventory_frame, width = 18)
        save_inventory_button = Button(inventory_frame, text = "Save", command = save_inventory, width = 3)
        show_inventory.pack()

        edit_button = Button(buttons_frame, text = "Edit", command = switch, width = 10)
        edit_button.pack(side= LEFT)
        delete_button = Button(buttons_frame, text = "Delete", command = delete, width = 10)
        delete_button.pack(side = LEFT)

    def submain_header(self):
        '''
        This func creat a header
        '''
        self.header = Frame(self.store_manager_frame, width = self.x)
        self.header.pack()
        code_label = Label(self.header, text = "Product code", width = 20).grid(column = 1, row = 0)
        name_label = Label(self.header, text = "Product name", width = 20).grid(column = 2, row = 0)
        price_label = Label(self.header, text = "Price", width = 20).grid(column = 3, row = 0)
        inventory_label = Label(self.header, text = "Inventory", width = 20).grid(column = 4, row = 0)
        extra_label = Label(self.header, width = 20).grid(column = 5, row = 0)

    def submain_show_data(self):
        '''
        This func show data as table
        Parent is store_manager_frame
        This func is pack by defaut
        '''
        self.show_data_frame = Frame(self.store_manager_frame, width = self.x, height = 50)
        self.show_data_frame.pack()
        #self.row_tool(0, self.show_data_frame)
        #scroll = Scrollbar(self.show_data_frame, command = self.show_data_frame.yview)
        #scroll.pack(side = RIGHT, fill = Y)
        #test_data_frame = Label(self.show_data_frame, text = "Helllo", width = self.x).pack()
        #scrollbar = Scrollbar(self.store_button_frame)
        #scrollbar.pack(side = RIGHT, fill = Y)
        #self.product_list = Listbox(self.show_data_frame, width = self.x).pack()
        #test_list = Label(self.product_list, text = "Helllo", width = self.x).place(x = 0, y = 10)
        #for index in range(0, len(self.data)):
        for index in range(0, len(self.data)):
            self.row_tool(index, self.show_data_frame)
            #scrollbar = Scrollbar(self.store_button_frame)
            #scrollbar.pack(side = RIGHT, fill = Y)
        #self.show_data_frame['yscrollcommand'] = scroll.get()

    def submain_search_result(self):
        '''
        This func creat a frame to show search rusult
        Parent is store_manager_frame
        This func is unpack by default
        When search_entry != 0, show_data_frame is unpack, search_result_frame is pack
        '''
        self.search_result_frame = Frame(self.store_manager_frame, width = self.x)

    def main_invoice_frame(self):
        '''
        This func creat main frame for invoice manager app
        Parent is self.w
        Invoice manager is unpack by default
        '''
        self.invoice_manager_frame = Frame(self.w, width = 800)
        test2 = Label(self.invoice_manager_frame, text = "Invoice").pack()
    

main_gui = window(800, 500)
main_gui.all_gui_funcs()
main_gui.w = mainloop()


################ Write into invoice csv ################
return_invoice_path = "db\invoice.csv"
return_invoice_file = open(return_invoice_path, "w", newline = "", encoding = "utf-8-sig")
invoice_writer = csv.writer(return_invoice_file)

invoice_writer.writerow(["Code", "Test", "123", "345", "Aloalo"])

for index in range(len(invoice_data)):
    invoice_writer.writerow(invoice_data[index])



################ Writer into main csv ################
return_path = "db\database.csv"
return_file = open(return_path, "w", newline = "", encoding = "utf-8-sig")
writer = csv.writer(return_file)

writer.writerow(["Code", "Name", "Price", "Inventory"])

for index in range(len(data)):
    writer.writerow(data[index])