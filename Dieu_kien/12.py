num = int(input())
if num == 1 or num == 2 or num ==3:
    print(f"{num} la so nguyen to")
else:
    i = 2
    while i < (num - 1):
        check = num % i
        if check == 0:
            num_type = "khong phai so nguyen to"
            break
        else:
            num_type = "la so nguyen to"
        i += 1
    print(f"{num} {num_type}")
    