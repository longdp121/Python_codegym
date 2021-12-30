
def remove_max_num(num_list):
    max_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
    return num_list.remove(max_num)
  

num_list = [8000, 2, 3, 44, 55555555, 689, 1, 100]
remove_max_num(num_list)
print(num_list)
