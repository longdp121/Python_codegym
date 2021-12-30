import datetime as dt

#Creat function
#1st module. Purpose is input new item
def sum_cost(em_list):  #Sub func
    '''
    This func sum all 3rd (index = 2) item of sub-list
    Result will be append to 1st (index = 0) item of main list (em_list)
    '''
    cost_take_out = 0
    for index in range(1, len(em_list)):
        cost_take_out += (em_list[index])[2]
    em_list[0].append("{:,}".format(cost_take_out))

def index_count(em_list):  #Sub func
    '''
    This func count every item in main list [0:]. Result is item order
    em_list[1] is first item
    Result will be append to last item in sub-list (index = -1)
    '''
    count = 1
    for index in range(1, len(em_list)):
        (em_list[index])[-1].append(count)
        count += 1

def update_list(em_list):  #Main func
    '''
    This func gives input for name, date, cost
    Sub-func are sum_cost(), index_count()
    '''
    while True:
        name = str(input("Please enter name: "))
        date = dt.datetime(int(input("Y: ")), int(input("M: ")), int(input("D: ")))
        date = date.strftime('%Y %b %d')
        cost = int(input("Please enter cost: "))
        new_list = [name, date, cost, []]
        em_list.append(new_list)
        close_func = str(input("Do you want to continue - y/n: "))
        while close_func not in ["y", "n"]:
            close_func = str(input("Do you want to continue - y/n: "))
        if close_func == "y":
            continue
        else:
            break
    for index in range(1, len(em_list)):
        (em_list[index])[-1] = []  #To clear order number. Avoid error when update list
    (em_list[0]).clear()  #To clear sumcost. Avoid error when update list
    sum_cost(em_list)
    index_count(em_list)
    #print()

#2nd module. Purpose is edit or del item
def select_item(em_list):  #Sub func
    '''
    This func select item in main list
    Based on item order by index_count()
    Return select
    '''
    while True:
        select = int(input("Enter item order: "))
        if 1 <= select < len(em_list):
            return select
        else:
            print("Range not found")
            continue

def delete_item(em_list):  #sub func
    '''
    This func delete select item
    Total cost and item order be renew when func ends
    '''
    for index in range(1, len(em_list)):
        (em_list[index])[-1] = []  #To clear order number. Avoid error when update list
    em_list.remove(em_list[select_item(em_list)])  #Remove item with number order given by select_item()
    (em_list[0]).clear()  #To clear sumcost. Avoid error when update list
    sum_cost(em_list)
    index_count(em_list)
    print("Item deleted.")

def edit_item(em_list):  #sub func
    '''
    This func edit items in main list
    Total cost be renew when func ends
    '''
    detail_edit = str(input("Please choose detail to edit: n for name, d for date, c for cost: "))
    while detail_edit not in ["n", "d", "c"]:
        detail_edit = str(input("Please choose detail to edit: n for name, d for date, c for cost: "))
    if detail_edit == "n":
        num = 0
        change = str(input("Enter new name: "))
    elif detail_edit == "d":
        num = 1
        change = str(input("Enter new date, format example: 2021 Nov 04: "))
    else:
        num = 2
        change = int(input("Enter new cost: "))
    (em_list[select_item(em_list)])[num] = change
    (em_list[0]).clear()  #To clear sumcost. Avoid error when update list
    sum_cost(em_list)
    print("Change saved.")
        
def change_list(em_list):  #main func
    '''
    This func edit or delete item
    Sub-func are delete_item() and edit_item()
    '''
    while True:
        choose_option = str(input("Please select e for edditing or d for delleting: "))
        while choose_option not in ["e", "d"]:
            choose_option = str(input("Please select e for edditing or d for delleting: "))
        if choose_option == "e":
           edit_item(em_list)
        else:
           delete_item(em_list)
        close_func = str(input("Do you want to continue - y/n: "))
        while close_func not in ["y", "n"]:
            close_func = str(input("Do you want to continue - y/n: "))
        if close_func == "y":
            continue
        else:
            break
    #print(em_list)


#3rd module. Main app
def main_app():
    print("Welcome to MyWallet!")
    em_list = [[]]
    while True:
        if len(em_list) == 1:
            print("Your list is emty")
            choose_option = str(input("Please choose n for add new item, x to exit: "))
            while choose_option not in ["n", "x"]:
                choose_option = str(input("Please choose n for add new item, x to exit: "))
            if choose_option == "n":
                update_list(em_list)
            else:
                break
        else:
            print()
            print(f"You have {len(em_list) -1} items.")
            print(em_list)
            choose_option = str(input("Please choose n for adding new item, c for changing, x to exit: "))
            while choose_option not in ["n", "c", "x"]:
                choose_option = str(input("Please choose n for adding new item, c for changing, x to exit: "))
            if choose_option == "n":
                update_list(em_list)
            elif choose_option == "c":
                change_list(em_list)
            else:
                break
    print("Exit and clear.")
            

#Main_app
main_app()
