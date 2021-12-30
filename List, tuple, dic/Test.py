
list_string = ["asbc", "a", "asc", "f", "fd"]
count = 0
for i in range (len(list_string) + 1):
    if len(list_string[i]) > 3:
        count += 1
print(count)

