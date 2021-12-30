#Creat function
def temp_exchange(num, unit):  #Give result
    if unit == "F":
        result = (num - 32) * (5/9)
    else:
        result = (num * (9/5)) + 32
    return round(result, 2)

def re_temp(unit):  #Give return unit
    if unit == "F":
        re_temp = "C"
    else:
        re_temp = "F"
    return re_temp

''''''
#Input
num = int(input("Enter any number: "))
unit = str(input("Please choose C or F: ").upper())

while unit not in ("C", "F"):
    unit = str(input("Please choose C or F: ").upper())

#Exchanging
print(f"{num}°{unit} = {temp_exchange(num, unit)}°{re_temp(unit)}")