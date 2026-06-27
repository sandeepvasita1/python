Write a python program that removes any repeated items 
from a list so that each item appears at most once. For 
instance,the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]. 

def unique_val(lst):
    r=[]
    for i in lst:
        if i not in r:
            r.append(i)
    print(r)

            
lst1=[4,5,4,5,2,1,3,1,6,6]
unique_val(lst1)
