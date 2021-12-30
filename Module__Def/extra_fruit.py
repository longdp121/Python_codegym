def more_fruit(fruit_list, extra):
    fruit_list.extend(extra)
    print(f"New fruit list is {fruit_list}")


fruit_list = ["mango", "water melon", "lemon", "apple"]
extra = ["dragon fruit", "qua buoi"]

more_fruit(fruit_list, extra)