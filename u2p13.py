Write a program to create nested list and display its 
elements. 
lst=[10,20,30,40]
lst2=[50,60,lst]

print(lst2[0])
print(lst2[1])
print(lst2[2])

for i in lst2[2]:
    print(i)

