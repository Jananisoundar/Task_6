list=[10,501,22,37,100,999,87,351]
odd=[]
even=[]
for n in list:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print("odd:", odd)
print("even:", even)
