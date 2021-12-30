#Creat function
def find_smallest_num(num_list):
    min_num = num_list[0]
    for i in num_list:
        if i < min_num:
            min_num = i
    return min_num

#Input
num_list = [11, 9, 222, 23, 100, 7, 98887, 4]

#Finding
print(f"The smallest number of this list {num_list} is ", find_smallest_num(num_list))