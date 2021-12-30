my_list = [1, 2, 3, 4, 5, 6, 7, 8, -2, - 6, -4]
index = 0
min_num_1 = 1  #Min num
min_num_2 = 2  #2nd min num
temp_num = None
for index in range(len(my_list)):
    temp_num = min_num_1
    if min_num_1 > my_list[index]:
        min_num_1 = my_list[index]
        min_num_2 = temp_num
    if min_num_2 > my_list[index] and my_list[index] > min_num_1:
        min_num_2 = my_list[index]
    else:
        pass

print(min_num_1, min_num_2)
