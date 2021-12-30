dept_db = {
      101 : 'HRD',
      102 : 'FINANCE',
      103 : 'ACCOUNTS',
      104 : 'SALES',
      105 : 'ENGINEERING',
      106 : 'SUPPORT'
     }
 

employee_db = { 
1000 : {"name" : "Alex",   "doj" : '01-10-89', "dept" : 103},
1001 : {"name" : "Mary",   "doj" : '01-11-88', "dept" : 101},
1002 : {"name" : "John",   "doj" : '01-10-87', "dept" : 104},
1003 : {"name" : "David",  "doj" : '01-06-89', "dept" : 105},
1004 : {"name" : "Anne",   "doj" : '01-01-86', "dept" : 106},
1005 : {"name" : "Samson", "doj" : '01-02-89', "dept" : 101}
}


def id_input(mydict):
    '''
    #This func check if input id is correct.
    #Return id if found
    '''
    emp_id = int(input("Please enter id: "))
    while emp_id not in mydict.keys():
        print("id not found")
        emp_id = int(input("Please enter id: "))
    return emp_id
        

def show_emp_info(mydict):
    '''
    This func show employee value
    Based on key give by id_input()
    '''
    return mydict[id_input(mydict)]

print(show_emp_info(employee_db))
