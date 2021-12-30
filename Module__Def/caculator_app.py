#Creat caculator function
def calc_app(num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    else:
        result = int(num1 / num2)
    return result

#Input
num1 = int(input("Enter any number: "))
op = str(input("Choose +, -, * or /: "))
while op not in ["+", "-", "*", "/"]:
    op = str(input("Choose +, -, * or /: "))
num2 = int(input("Enter any number: "))

#Cacultate
calc_app(num1, op, num2)
print(f"{num1} {op} {num2} =", calc_app(num1, op, num2))