gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 'Television', 1000, 'Laptop Case', 'Camera Lens']
num = []
txt = []
for index in gadgets:
    if isinstance(index, str):
        txt.append(index)
    elif isinstance(index, int) or isinstance(index, float):
        num.append(index)

#print results

print(f"All strings in list are {num}")
print(f"All int and float in list are {txt}")

num.sort()
txt.sort()
print(f"List of number with ascending is {num}")
print(f"Txt list with alphabet order is {txt}")

num.sort(reverse=True)
txt.sort(reverse=True)
print(f"Number list with reversed order is {num}")
print(f"Txt list with reversed order is {txt}")