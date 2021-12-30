#Creat function for sorting number
def number_order(num1, num2, num3):
    list_num = [num1, num2, num3]
    #When 3 equal
    if num1 == num2 == num3:
        max_num = mid_num = min_num = num1

    #When 2 equal
    elif num1 == num2 or num2 == num3 or num3 == num1:
        if num1 == num2:
            if num3 > num2:
                max_num = num3
                mid_num = min_num = num1
            else:
                max_num = mid_num = num1
                min_num = num3
        elif num2 == num3:
            if num1 > num2:
                max_num = num1
                mid_num = min_num = num3
            else:
                max_num = mid_num = num3
                min_num = num1
        else:
            if num2 > num1:
                max_num = num2
                mid_num = min_num = num3
            else:
                max_num = mid_num = num1
                min_num = num2

    else:  #When no equal
        if num1 > num2 and num1 > num3:  #1 max
            max_num = num1
            if num2 > num3:
                mid_num = num2
                min_num = num3
            else:
                mid_num = num3
                min_num = num2
        elif num2 > num1 and num2 > num3:  #2 max
            max_num = num2
            if num1 > num3:
                mid_num = num1
                mid_num = num3
            else:
                mid_num = num3
                min_num = num1
        else:  #3 max
            max_num = num3
            if num1 > num2:
                mid_num = num1
                min_num = num2
            else:
                mid_num = num2
                min_num = num1
    print(f"Great and greater order of this list {list_num} is:\n")
    print([min_num, mid_num, max_num])
    
#Input
num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))

#Sorting
number_order(num1, num2, num3)