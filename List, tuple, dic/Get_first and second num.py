my_list = [1, 2, 3, 4, 587615334, 6, 7, 11, 100, 2412, 134, 3133, 4135, 341348, 134]
#my_list = [1000]


if len(my_list) > 1:
    my_list.sort()
    result_list = my_list[-2:]
    result_list.sort(reverse=True)

else:
    result_list = my_list[0]

print(f"Largest and second largest num in given list is {result_list}")