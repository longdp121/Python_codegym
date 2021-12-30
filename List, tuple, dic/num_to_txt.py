num = (input("Enter any number: "))
txt = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

for n in num:
    print(txt[int(n)], end = " ")