my_list = [1, 2, 3, 4, 5, 6]
other = [6, 5, 4, 3, 2, 1]
def hehe():
    for index in range(0, 6):
        my_list[index] = (10 * other[index])
    return my_list

print(my_list)