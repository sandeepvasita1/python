Create a program to search the position of an element in 
an array using index() method of array class. 

import array as ar
arr=ar.array('i',[2,5,8,7,9,2,1,6,7,5])

print(arr)

se=int(input("enter value to be search:"))

if se in arr:
    p=arr.index(se)
    print(f"{se} value position is {p}")

else:
    print(f"{se} value position is not found")
