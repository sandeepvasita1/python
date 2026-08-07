Write a program to find out and display the common and 
the non common elements in the list using membership 
operators 

list1=[10,20,30,40,50]
list2=[30,40,50,60,70]

common = []
non_common = []

for i in list1:
    if i in list2:
        common.append(i)

        
for i in list1:
    if i not in list2:
        non_common.append(i)


for i in list2:
    if i not in list1:
        non_common.append(i)


print("common element:",common)
print("non_common element:",non_common)
