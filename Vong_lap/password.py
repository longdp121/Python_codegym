def try_time(c):
    '''
    This func give time or times based on number of try
    '''
    txt = ["time", "times"]
    if c == 1:
        return txt[0]
    else:
        return txt[1]

def remain_time(c, t):
    '''
    This func give time or times based on number of remain
    Lock if count == try_limit
    '''
    txt = ["time", "times"]
    if c < t:
        if c == t - 1:
            return f"{t - c} {txt[0]} remain"
        else:
            return f"{t - c} {txt[1]} ramain"
    elif c == t:
        return("Account lock")

def password_input():
    #This func give password input
    return str(input("Enter password: "))

passw = "DayLaMatKhau_"
en_passw = password_input()
try_limit = 3
count = 0
while True:
    if en_passw == passw:
        if count < try_limit:
            print("Welcome")
            break
        else:
            print("Deactive")
            en_passw = password_input()
    else:
        if 0 <= count < try_limit:
            count += 1
            print(count)
            print(f"Wrong password. You have tried {count} {try_time(count)}, {remain_time(count, try_limit)}")
            en_passw = password_input()
        else:
            print("Deactive")
            en_passw = password_input()