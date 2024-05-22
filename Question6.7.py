list = [10, 501, 22, 37, 100, 999, 87, 100, 501]
list2 = []
list3 = []
for n in list:
    if n not in list2:
        list2.append(n)
    else:
        list3.append(n)

print(list2)
print("The first duplicate number in the given:", list3[0])
