Write a program to find out and display the common and 
the non common elements in the list using membership 
operators 

list1=[10,20,30,40,50]
list2=[30,40,50,60,70]

common = []
non_common = []

for item in list1:
    if item in list2:
        common.append(item)

        
for item in list1:
    if item not in list2:
        non_common.append(item)


for item in list2:
    if item not in list1:
        non_common.append(item)


print("common element:",common)
print("non_common element:",non_common)
