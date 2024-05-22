list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
Compare_list_of_list1andlist2 = []
Compare_list_of_list1_list2_with_list3 = []

for l1 in list1:
    for l2 in list2:
        if l1 == l2:
            Compare_list_of_list1andlist2.append(l1)
for n in Compare_list_of_list1andlist2:
    for l3 in list3:
        if n == l3:
            Compare_list_of_list1_list2_with_list3.append(n)

print(Compare_list_of_list1andlist2)
print("Duplicate in all three list:", Compare_list_of_list1_list2_with_list3)
